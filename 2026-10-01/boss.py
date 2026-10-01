# The Assize of the Hanging Oak
# 
# WARNING TO THE GUILD: The Assize of the Hanging Oak
# 
# North of Bitwick the road runs through Wrenfold Wood. At the heart of the wood stands the Hanging Oak,
# and each night a court of long-dead magistrates sits beneath it. This court, the Assize, judges every
# traveller who crosses its clearing. It judges by edicts carved into the bark over many centuries,
# and newer carvings strike out older ones. The Assize is not cruel, only exact. Before the guild sends
# anyone down that road, the inn wants every verdict known in advance.
# 
# Write assize_verdicts(edicts, travellers). It returns a list of strings holding the verdicts for the travellers,
# in the order the travellers are given.
# 
# Edicts. edicts is a list. An edict's *index* is its 0-based position in that list. Each edict is an object
# with exactly these keys: - rank: an integer, which may be negative. - when: an object mapping attribute names
# to string values. It may be empty. - verdict: a string. - repeals: a list of integer indices. Every index in it is
# smaller than this edict's own index. The list may be empty. - limit: a non-negative integer, or null for no limit.
# 
# Travellers. travellers is a list of objects, each mapping attribute names to string values.
# The travellers reach the clearing in list order.
# 
# Rule 1: standing. Which edicts *stand* is decided once, before any traveller is judged. Edict i stands unless
# some edict j that itself stands lists i in its repeals. A repeal made by an edict that does not stand has no
# effect. Because every repeal points to an earlier edict, this is well defined. An edict that does not stand plays
# no further part.
# 
# Rule 2: matching. An edict *matches* a traveller when, for every key in the edict's when, the traveller has that
# key and its value is exactly equal to the edict's value. Comparison is case-sensitive, and an empty string is a real value.
# An empty when matches every traveller. Attributes the traveller has that are not in when are ignored.
# 
# Rule 3: precedence. For each traveller, the *candidates* are the edicts that stand, match the traveller, and are
# not exhausted (see Rule 4). The *deciding* edict is chosen as follows:
#   1. Take the candidate with the highest rank.
#   2. If several share that rank, take the one with the most keys in when.
#   3. If several are still tied, take the one with the highest index.
# 
# The traveller's verdict is the deciding edict's verdict, returned unchanged. If there are no candidates,
# the verdict is "pass".
# 
# Rule 4: exhaustion. Travellers are judged one at a time, in order. An edict whose limit is an integer may
# be the deciding edict for at most limit travellers in total. Once it has decided that many, it is *exhausted* and
# is not a candidate for any later traveller. An edict with limit 0 never decides. An edict with limit null never exhausts.
# Exhaustion never changes which edicts stand: a repeal made by an exhausted edict stays in effect.


def assize_verdicts(edicts, travellers):
    verdicts = []
    edicts_r1 = list(range(len(edicts)))
    # R1: standing
    index = len(edicts) - 1
    for edict in reversed(edicts):
        if index in edicts_r1:
            for repeal in edict["repeals"]:
                if repeal in edicts_r1:
                    edicts_r1.remove(repeal)
        index -= 1

    # R4: exhaustion - set limits list
    edict_limits = []
    for i in range(len(edicts)):
        edict_limits.append(edicts[i]["limit"])

    for traveller in travellers:
        edicts_r2 = []
        # R2: matching
        for edict_index in edicts_r1:
            if edicts[edict_index]["when"].keys() <= traveller.keys():
                all_match = True
                for key in edicts[edict_index]["when"].keys():
                    if edicts[edict_index]["when"][key] != traveller[key]:
                        all_match = False
                        break
                if all_match:
                    edicts_r2.append(edict_index)

        # R4: exhaustion - pre
        edicts_r4 = []
        for er in edicts_r2:
            if edict_limits[er] == None or edict_limits[er] > 0:
                edicts_r4.append(er)
        
        # R3: precedence
        sorted_edicts = sorted(edicts_r4, key=lambda edt: (edicts[edt]["rank"], len(edicts[edt]["when"]), edt), reverse=True)
        if len(sorted_edicts) == 0:
            verdicts.append('pass')
            continue

        # R4: exhaustion - post
        verdicts.append(edicts[sorted_edicts[0]]["verdict"])

        if edict_limits[sorted_edicts[0]] is not None:
            edict_limits[sorted_edicts[0]] -= 1

    return verdicts