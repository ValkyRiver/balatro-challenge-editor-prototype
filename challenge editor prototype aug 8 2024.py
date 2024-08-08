jokerlist = ["joker", "greedy_joker", "lusty_joker", "wrathful_joker", "gluttonous_joker", "jolly", "zany", "mad", "crazy", "droll", "sly", "wily", "clever", "devious", "crafty", "half",
             "stencil", "four_fingers", "mime", "credit_card", "ceremonial", "banner", "mystic_summit", "marble", "loyalty_card", "8_ball", "misprint", "dusk", "raised_fist", "chaos",
             "fibonacci", "steel_joker", "scary_face", "abstract", "delayed_grat", "hack", "pareidolia", "gros_michel", "even_steven", "odd_todd", "scholar", "business_card", "supernova",
             "ride_the_bus", "space", "egg", "burglar", "blackboard", "runner", "ice_cream", "dna", "splash", "blue_joker", "sixth_sense", "constellation", "hiker", "faceless",
             "green_joker", "superposition", "todo_list", "cavendish", "card_sharp", "red_card", "madness", "square", "seance", "riff_raff", "vampire", "shortcut", "hologram", "vagabond",
             "baron", "cloud_9", "rocket", "obelisk", "midas_mask", "luchador", "photograph", "gift", "turtle_bean", "erosion", "reserved_parking", "mail", "to_the_moon", "hallucination",
             "fortune_teller", "juggler", "drunkard", "stone", "golden", "lucky_cat", "baseball", "bull", "diet_cola", "trading", "flash", "popcorn", "trousers", "ancient", "ramen",
             "walkie_talkie", "selzer", "castle", "smiley", "campfire", "ticket", "mr_bones", "acrobat", "sock_and_buskin", "swashbuckler", "troubadour", "certificate", "smeared",
             "throwback", "hanging_chad", "rough_gem", "bloodstone", "arrowhead", "onyx_agate", "glass", "ring_master", "flower_pot", "blueprint", "wee", "merry_andy", "oops", "idol",
             "seeing_double", "matador", "hit_the_road", "duo", "trio", "family", "order", "tribe", "stuntman", "invisible", "brainstorm", "satellite", "shoot_the_moon", "drivers_license",
             "cartomancer", "astronomer", "burnt", "bootstraps", "caino", "triboulet", "yorick", "chicot", "perkeo"] #prefix: j_
tarotlist = ["fool", "magician", "high_priestess", "empress", "emperor", "heirophant", "lovers", "chariot", "justice", "hermit", "wheel", "strength", "hanged_man", "death", "temperence",
             "devil", "tower", "star", "moon", "sun", "judgement", "world"]
planetlist = ["pluto", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "planet_x", "ceres", "eris"]
spectrallist = ["familiar", "grim", "incantation", "talisman", "aura", "wraith", "sigil", "ouija", "ectoplasm", "immolate", "ankh", "deja_vu", "hex", "trance", "medium", "cryptid",
                "soul", "black_hole"]
consumablelist = tarotlist + planetlist + spectrallist #prefix: c_
packlist = ["arcana_normal_1", "arcana_normal_2", "arcana_normal_3", "arcana_normal_4", "arcana_jumbo_1", "arcana_jumbo_2", "arcana_mega_1", "arcana_mega_2",
            "celestial_normal_1", "celestial_normal_2", "celestial_normal_3", "celestial_normal_4", "celestial_jumbo_1", "celestial_jumbo_2", "celestial_mega_1", "celestial_mega_2",
            "standard_normal_1", "standard_normal_2", "standard_normal_3", "standard_normal_4", "standard_jumbo_1", "standard_jumbo_2", "standard_mega_1", "standard_mega_2",
            "buffoon_normal_1", "buffoon_normal_2", "buffoon_jumbo_1", "buffoon_mega_1", "spectral_normal_1", "spectral_normal_2", "spectral_jumbo_1", "spectral_mega_1"] #prefix: p_
voucherlist = ["overstock_norm", "overstock_plus", "hone", "glow_up", "clearance_sale", "liquidation", "crystal_ball", "omen_globe", "grabber",
               "nacho_tong", "telescope", "observatory", "wasteful", "recyclomancy", "tarot_merchant", "tarot_tycoon", "seed_money", "money_tree", "planet_merchant", "planet_tycoon",
               "blank", "antimatter", "magic_trick", "illusion", "directors_cut", "retcon", "hieroglyph", "petroglyph", "paint_brush", "palette"] #prefix: v_
taglist = ["uncommon", "rare", "negative", "foil", "holo", "polychrome", "investment", "voucher", "boss", "standard", "charm", "meteor", "buffoon", "handy", "garbage", "ethereal",
           "coupon", "double", "juggle", "d_six", "top_up", "skip", "orbital", "economy"] #prefix: tag_
blindlist = ["hook", "ox", "house", "wall", "wheel", "arm", "club", "fish", "psychic", "goad", "water", "window", "manacle", "eye", "mouth", "plant", "serpent", "pillar", "needle", "head",
             "tooth", "flint", "mark", "final_acorn", "final_leaf", "final_vessel", "final_heart", "final_bell"] #prefix: bl_

modifiersdefault = [["joker_slots", "5"], ["consumable_slots", "2"], ["hand_size", "8"], ["hands", "4"], ["discards", "3"], ["dollars", "4"], ["reroll_cost", "5"]]
deckdefault = [["A", "S", "unenh", "base", "Noseal"], ["K", "S", "unenh", "base", "Noseal"], ["Q", "S", "unenh", "base", "Noseal"], ["J", "S", "unenh", "base", "Noseal"],
               ["T", "S", "unenh", "base", "Noseal"], ["9", "S", "unenh", "base", "Noseal"], ["8", "S", "unenh", "base", "Noseal"], ["7", "S", "unenh", "base", "Noseal"],
               ["6", "S", "unenh", "base", "Noseal"], ["5", "S", "unenh", "base", "Noseal"], ["4", "S", "unenh", "base", "Noseal"], ["3", "S", "unenh", "base", "Noseal"],
               ["2", "S", "unenh", "base", "Noseal"], #spades
               ["A", "H", "unenh", "base", "Noseal"], ["K", "H", "unenh", "base", "Noseal"], ["Q", "H", "unenh", "base", "Noseal"], ["J", "H", "unenh", "base", "Noseal"],
               ["T", "H", "unenh", "base", "Noseal"], ["9", "H", "unenh", "base", "Noseal"], ["8", "H", "unenh", "base", "Noseal"], ["7", "H", "unenh", "base", "Noseal"],
               ["6", "H", "unenh", "base", "Noseal"], ["5", "H", "unenh", "base", "Noseal"], ["4", "H", "unenh", "base", "Noseal"], ["3", "H", "unenh", "base", "Noseal"],
               ["2", "H", "unenh", "base", "Noseal"], #hearts
               ["A", "C", "unenh", "base", "Noseal"], ["K", "C", "unenh", "base", "Noseal"], ["Q", "C", "unenh", "base", "Noseal"], ["J", "C", "unenh", "base", "Noseal"],
               ["T", "C", "unenh", "base", "Noseal"], ["9", "C", "unenh", "base", "Noseal"], ["8", "C", "unenh", "base", "Noseal"], ["7", "C", "unenh", "base", "Noseal"],
               ["6", "C", "unenh", "base", "Noseal"], ["5", "C", "unenh", "base", "Noseal"], ["4", "C", "unenh", "base", "Noseal"], ["3", "C", "unenh", "base", "Noseal"],
               ["2", "C", "unenh", "base", "Noseal"], #clubs
               ["A", "D", "unenh", "base", "Noseal"], ["K", "D", "unenh", "base", "Noseal"], ["Q", "D", "unenh", "base", "Noseal"], ["J", "D", "unenh", "base", "Noseal"],
               ["T", "D", "unenh", "base", "Noseal"], ["9", "D", "unenh", "base", "Noseal"], ["8", "D", "unenh", "base", "Noseal"], ["7", "D", "unenh", "base", "Noseal"],
               ["6", "D", "unenh", "base", "Noseal"], ["5", "D", "unenh", "base", "Noseal"], ["4", "D", "unenh", "base", "Noseal"], ["3", "D", "unenh", "base", "Noseal"],
               ["2", "D", "unenh", "base", "Noseal"]] #diamonds

decklist = ["Red", "Blue", "Yellow", "Green", "Black", "Magic", "Nebula", "Ghost", "Abandoned", "Checkered", "Zodiac", "Painted", "Anaglyph", "Plasma", "Erratic", "Challenge"]
editionlist = ["base", "foil", "holo", "poly", "neg"]
stickerlist = ["none", "eter", "per", "rent", "eterent", "perent"]
enhancementlist = ["unenh", "bonus", "mult", "wild", "glass", "steel", "stone", "gold", "lucky"]
seallist = ["Noseal", "Gold", "Red", "Blue", "Purple"]

customruleslist = ["no_reward", "no_extra_hand_money", "no_interest"] #this list in incomplete and requires expansion

header = ["testchallenge", "testchallenge", "author", "created using ValkyRiver's challenge editor prototype"] #steammodded header: name, id, author, description
customrules = []
modifiers = list(modifiersdefault)
jokers = []
consumables = []
vouchers = []
deck = list(deckdefault)
decktype = "Challenge"
bannedjokers = []
bannedconsumables = []
bannedvouchers = []
bannedpacks = []
bannedtags = []
bannedblinds = []

def luajoker(joker, edition, sticker):
    if edition == "foil":
        e = ", edition = 'foil'"
    elif edition == "holo":
        e = ", edition = 'holo'"
    elif edition == "poly":
        e = ", edition = 'polychrome'"
    elif edition == "neg":
        e = ", edition = 'negative'"
    else:
        e = ""
    if sticker == "eter":
        s = ", eternal = true"
    elif sticker == "per":
        s = ", perishable = true"
    elif sticker == "rent":
        s = ", rental = true"
    elif sticker == "eterent":
        s = ", eternal = true, rental = true"
    elif sticker == "perent":
        s = ", perishable = true, rental = true"
    else:
        s = ""
    return "      {id = 'j_"+joker+"'"+e+s+"},"

def luaconsumable(consumable, edition):
    if edition == "foil":
        e = ", edition = 'foil'"
    elif edition == "holo":
        e = ", edition = 'holo'"
    elif edition == "poly":
        e = ", edition = 'polychrome'"
    elif edition == "neg":
        e = ", edition = 'negative'"
    else:
        e = ""
    return "      {id = 'c_"+consumable+"'"+e+"},"

def luacard(rank, suit, enhancement, edition, seal):
    if enhancement == "unenh":
        enh = ""
    else:
        enh = ", e = 'm_"+enhancement+"'"
    if edition == "foil":
        e = ", d = 'foil'"
    elif edition == "holo":
        e = ", d = 'holo'"
    elif edition == "poly":
        e = ", d = 'polychrome'"
    elif edition == "neg":
        e = ", d = 'negative'"
    else:
        e = ""
    if seal == "Noseal":
        s = ""
    else:
        s = ", g = '"+seal+"'"
    return "        {r = '"+rank+"', s = '"+suit+"'"+enh+e+s+"},"

def printmod(header, customrules, modifiers, jokers, consumables, vouchers, deck, decktype, bannedjokers, bannedconsumables, bannedvouchers, bannedpacks, bannedtags, bannedblinds):
    print("--- STEAMODDED HEADER\n--- MOD_NAME: "+header[0]+"\n--- MOD_ID: "+header[1]+"\n--- MOD_AUTHOR: ["+header[2]+"]\n--- MOD_DESCRIPTION: "+header[3]+"\n") #steammodded header
    print("----------------------------------------------\n------------MOD CODE -------------------------\n\n")
    print("function SMODS.INIT."+header[1]+" ()\n") #initialization
    print("  local challenges = G.CHALLENGES\n    G.localization.misc.challenge_names[\"c_mod_"+header[1]+"\"] = \""+header[0]+"\"\n") 
    print("  table.insert(G.CHALLENGES,#G.CHALLENGES+1,{\n    name = '"+header[0]+"',\n    id = 'c_mod_"+header[1]+"',\n    rules = {")
    if len(customrules) == 0: #customrules
        print("      custom = {},")
    else:
        print("      custom = {")
        for customrule in customrules:
            print("        {id = '"+customrule+"'},")
        print("      },")
    print("      modifiers = {") #modifiers
    for modifier in modifiers:
        print("        {id = '"+modifier[0]+"', value = "+modifier[1]+"},")
    print("      },\n    },")
    if len(jokers) == 0: #jokers
        print("    jokers = {},")
    else:
        print("    jokers = {")
        for joker in jokers:
            print(luajoker(joker[0], joker[1], joker[2]))
        print("    },")
    if len(consumables) == 0: #consumables
        print("    consumeables = {},")
    else:
        print("    consumeables = {")
        for consumable in consumables:
            print(luaconsumable(consumable[0], consumable[1]))
        print("    },")
    if len(vouchers) == 0: #vouchers
        print("    vouchers = {},")
    else:
        print("    vouchers = {")
        for voucher in vouchers:
            print("      {id = 'v_"+voucher+"'},")
        print("    },")
    print("    deck = {")
    if len(deck) == 0: #cards
        print("      cards = {},")
    else:
        print("      cards = {")
        for card in deck:
            print(luacard(card[0], card[1], card[2], card[3], card[4]))
        print("      },")
    print("      type = '"+decktype+" Deck',") #decktype
    print("    },")
    print("    restrictions = {")
    if len(bannedjokers) + len(bannedconsumables) + len(bannedvouchers) + len(bannedpacks) == 0:
        print("      banned_cards = {},")
    else:
        print("      banned_cards = {")
        for joker in bannedjokers: #bannedjokers
            print("      {id = 'j_"+joker+"'},")
        for consumable in bannedconsumables: #bannedconsumables
            print("      {id = 'c_"+consumable+"'},")
        for voucher in bannedvouchers: #bannedvouchers
            print("      {id = 'v_"+voucher+"'},")
        for pack in bannedpacks: #bannedpacks
            print("      {id = 'p_"+pack+"'},")
        print("      },")
    if len(bannedtags) == 0:  #bannedtags
        print("      banned_tags = {},")
    else:
        print("      banned_tags = {")
        for tag in bannedtags:
            print("      {id = 'tag_"+tag+"},")
        print("      },")
    if len(bannedblinds) == 0: #bannedblinds
        print("      banned_other = {},")
    else:
        print("      banned_other = {")
        for blind in bannedblinds:
            print("        {id = 'bl_"+blind+"'},")
        print("        },")
    print("    },\n  })\n\nend\n")

def export(header, customrules, modifiers, jokers, consumables, vouchers, deck, decktype, bannedjokers, bannedconsumables, bannedvouchers, bannedpacks, bannedtags, bannedblinds):
    f = open(header[0]+".lua", "a")
    f.write("--- STEAMODDED HEADER\n--- MOD_NAME: "+header[0]+"\n--- MOD_ID: "+header[1]+"\n--- MOD_AUTHOR: ["+header[2]+"]\n--- MOD_DESCRIPTION: "+header[3]+"\n") #steammodded header
    f.write("----------------------------------------------\n------------MOD CODE -------------------------\n\n\n")
    f.write("function SMODS.INIT."+header[1]+" ()\n\n") #initialization
    f.write("  local challenges = G.CHALLENGES\n    G.localization.misc.challenge_names[\"c_mod_"+header[1]+"\"] = \""+header[0]+"\"\n\n") 
    f.write("  table.insert(G.CHALLENGES,#G.CHALLENGES+1,{\n    name = '"+header[0]+"',\n    id = 'c_mod_"+header[1]+"',\n    rules = {\n")
    if len(customrules) == 0: #customrules
        f.write("      custom = {},\n")
    else:
        f.write("      custom = {\n")
        for customrule in customrules:
            f.write("        {id = '"+customrule+"'},\n")
        f.write("      },\n")
    f.write("      modifiers = {\n") #modifiers
    for modifier in modifiers:
        f.write("        {id = '"+modifier[0]+"', value = "+modifier[1]+"},\n")
    f.write("      },\n    },\n")
    if len(jokers) == 0: #jokers
        f.write("    jokers = {},\n")
    else:
        f.write("    jokers = {\n")
        for joker in jokers:
            f.write(luajoker(joker[0], joker[1], joker[2])+"\n")
        f.write("    },\n")
    if len(consumables) == 0: #consumables
        f.write("    consumeables = {},\n")
    else:
        f.write("    consumeables = {\n")
        for consumable in consumables:
            f.write(luaconsumable(consumable[0], consumable[1])+"\n")
        f.write("    },\n")
    if len(vouchers) == 0: #vouchers
        f.write("    vouchers = {},\n")
    else:
        f.write("    vouchers = {\n")
        for voucher in vouchers:
            f.write("      {id = 'v_"+voucher+"'},\n")
        f.write("    },\n")
    f.write("    deck = {\n")
    if len(deck) == 0: #cards
        f.write("      cards = {},\n")
    else:
        f.write("      cards = {\n")
        for card in deck:
            f.write(luacard(card[0], card[1], card[2], card[3], card[4])+"\n")
        f.write("      },\n")
    f.write("      type = '"+decktype+" Deck',\n") #decktype
    f.write("    },\n")
    f.write("    restrictions = {\n")
    if len(bannedjokers) + len(bannedconsumables) + len(bannedvouchers) + len(bannedpacks) == 0:
        f.write("      banned_cards = {},\n")
    else:
        f.write("      banned_cards = {\n")
        for joker in bannedjokers: #bannedjokers
            f.write("      {id = 'j_"+joker+"'},\n")
        for consumable in bannedconsumables: #bannedconsumables
            f.write("      {id = 'c_"+consumable+"'},\n")
        for voucher in bannedvouchers: #bannedvouchers
            f.write("      {id = 'v_"+voucher+"'},\n")
        for pack in bannedpacks: #bannedpacks
            f.write("      {id = 'p_"+pack+"'},\n")
        f.write("      },\n")
    if len(bannedtags) == 0:  #bannedtags
        f.write("      banned_tags = {},\n")
    else:
        f.write("      banned_tags = {\n")
        for tag in bannedtags:
            f.write("      {id = 'tag_"+tag+"},\n")
        f.write("      },\n")
    if len(bannedblinds) == 0: #bannedblinds
        f.write("      banned_other = {},\n")
    else:
        f.write("      banned_other = {\n")
        for blind in bannedblinds:
            f.write("        {id = 'bl_"+blind+"'},\n")
        f.write("      },\n")
    f.write("    },\n  })\n\nend")    
    f.close()

command = ""

while True:
    command = input("> ")
    C = command.split(" ")
    if C[0] == "help":
        print("""Commands:
- help
- start joker [joker] [edition: base/foil/holo/poly/neg] [sticker: none/eter/per/rent/eterent/perent]
- start consumable [consumable] [edition: base/foil/holo/poly/neg]
- start voucher [voucher]
- start remove [joker/consumable/voucher]
- start list
- ban joker [joker]
- ban consumable [consumable]
- ban voucher [voucher]
- ban pack [pack]
- ban tag [tag]
- ban blind [blind]
- ban remove [joker/consumable/voucher/pack/tag/blind]
- ban list
- deck add [rank: A/K/Q/J/T/9/8/7/6/5/4/3/2] [suit: S/H/C/D] [enhancement: unenh/bonus/mult/wild/glass/steel/stone/gold/lucky] [edition: base/foil/holo/poly/neg]
  [seal: Noseal/Gold/Red/Blue/Purple]
- deck remove [rank: A/K/Q/J/T/9/8/7/6/5/4/3/2] [suit: S/H/C/D] [enhancement: unenh/bonus/mult/wild/glass/steel/stone/gold/lucky] [edition: base/foil/holo/poly/neg]
  [seal: Noseal/Gold/Red/Blue/Purple]
- deck default
- deck clear
- deck type [type: Red/Blue/Yellow/Green/Black/Magic/Nebula/Ghost/Abandoned/Checkered/Zodiac/Painted/Anaglyph/Plasma/Erratic/Challenge]
- deck list
- modifier [modifier: joker_slots/hand_size/consumable_slots/hands/discards/dollars/reroll_cost] [value]
- modifier default
- modifier list
- customrules add [customrule]
- customrules remove [customrule]
- customrules list
- header name [name]
- header id [id]
- header author [author]
- header description [description]
- header list
- list [jokers/tarots/planets/spectrals/vouchers/packs/tags/blinds]
- print
- export
    """)
    elif C[0] == "start":
        if (C[1] == "joker") and (C[2] in jokerlist) and (C[3] in editionlist) and (C[4] in stickerlist):
            jokers.append([C[2], C[3], C[4]])
            if C[3] == "base":
                    e = ""
            else:
                e = C[3]+" "
            if C[4] == "none":
                s = ""
            else:
                s = C[4]+" "
            print("Added a", s+e+C[2], "to initial joker loadout\n")
        elif (C[1] == "consumable") and (C[2] in consumablelist and (C[3] in editionlist)):
            consumables.append([C[2], C[3]])
            if C[3] == "base":
                    e = ""
            else:
                e = C[3]+" "
            print("Added a", e+C[2], "to initial consumable loadout\n")
        elif (C[1] == "voucher") and (C[2] in voucherlist):
            if C[2] in vouchers:
                print(C[2], "is already in initial vouchers\n")
            elif C[2] in ["reroll_glut", "reroll_surplus"]:
                print("Reroll Glut and Reroll Surplus are known to cause crashes. Try modifier reroll_cost 3 or modifier reroll_cost 1 respectively instead.\n")
            else:
                vouchers.append(C[2]); print("Added", C[2], "to initial vouchers\n")
        elif C[1] == "remove":
            jokers2 = list(jokers); consumables2 = list(consumables); jsuccess = False; csuccess = False; vsuccess = False
            for j, joker in enumerate(jokers):
                if C[2] in joker:
                    jokers2.pop(j); jsuccess = True
            consumables2 = list(consumables)
            for c, consumable in enumerate(consumables):
                if C[2] in consumable:
                    consumables2.pop(c); csuccess = True
            if C[2] in vouchers:
                vouchers.remove(C[2]); vsuccess = True
            jokers = list(jokers2)
            consumables = list(consumables2)
            if (jsuccess or csuccess or vsuccess):
                print("Removed", C[2], "from initial loadout\n")
            else:
                print("Could not locate this item\n")
        elif C[1] == "list":
            comprehendjokers = []; comprehendconsumables = []
            for joker in jokers:
                if joker[1] == "base":
                    e = ""
                else:
                    e = joker[1]+" "
                if joker[2] == "none":
                    s = ""
                else:
                    s = joker[2]+" "
                comprehendjokers.append(s+e+joker[0])
            for consumable in consumables:
                if consumable[1] == "base":
                    e = ""
                else:
                    e = consumable[1]+" "
                comprehendconsumables.append(e+consumable[0])
            print("Starting jokers:", ", ".join(comprehendjokers))
            print("Starting consumables:", ", ".join(comprehendconsumables))
            print("Starting vouchers:", ", ".join(vouchers))
            print()
        else:
            print("""Invalid command. Try start joker [joker] [edition: base/foil/holo/poly/neg] [sticker: none/eter/per/rent/eterent/perent], start consumable [consumable]
[edition: base/foil/holo/poly/neg]\n, start voucher [voucher], start remove [joker/consumable/voucher], or start list.\n""")
    elif C[0] == "ban":
        if (C[1] == "joker") and (C[2] in jokerlist):
            if C[2] in bannedjokers:
                print(C[2], "is already in the jokers banlist")
            else:
                bannedjokers.append(C[2]); print("Added", C[2], "to banned jokers\n")
        elif (C[1] == "consumable") and (C[2] in consumablelist):
            if C[2] in bannedconsumables:
                print(C[2], "is already in the consumables banlist\n")
            else:
                bannedconsumables.append(C[2]); print("Added", C[2], "to banned consumables\n")
        elif (C[1] == "voucher") and (C[2] in voucherlist):
            if C[2] in bannedvouchers:
                print(C[2], "is already in the vouchers banlist\n")
            else:
                bannedvouchers.append(C[2]); print("Added", C[2], "to banned vouchers\n")
        elif (C[1] == "pack") and (C[2] in packlist):
            if C[2] in bannedpacks:
                print(C[2], "is already in the packs banlist\n")
            else:
                bannedpacks.append(C[2]); print("Added", C[2], "to banned packs\n")
        elif (C[1] == "tag") and (C[2] in taglist):
            if C[2] in bannedtags:
                print(C[2], "is already in the tags banlist\n")
            else:
                bannedpacks.append(C[2]); print("Added", C[2], "to banned tags\n")
        elif (C[1] == "blind") and (C[2] in blindlist):
            if C[2] in bannedblinds:
                print(C[2], "is already in the blinds banlist\n")
            else:
                bannedblinds.append(C[2]); print("Added", C[2], "to banned blinds\n")
        elif C[1] == "remove":
            if C[2] in bannedjokers:
                bannedjokers.remove(C[2])
            elif C[2] in bannedconsumables:
                bannedconsumables.remove(C[2])
            elif C[2] in bannedvouchers:
                bannedvouchers.remove(C[2])
            elif C[2] in bannedpacks:
                bannedpacks.remove(C[2])
            elif C[2] in bannedtags:
                bannedtags.remove(C[2])
            else:
                print("Could not locate this item\n")
        elif C[1] == "list":
            print("Banned jokers:", ", ".join(bannedjokers))
            print("Banned consumables:", ", ".join(bannedconsumables))
            print("Banned vouchers:", ", ".join(bannedvouchers))
            print("Banned packs:", ", ".join(bannedpacks))
            print("Banned tags:", ", ".join(bannedtags))
            print()
        else:
            print("""Invalid command. Try ban joker [joker], ban consumable [consumable], ban voucher [voucher], ban pack [pack], ban tag [tag], ban blind [blind], or ban remove
[joker/consumable/voucher/pack/tag/blind].\n""")
    elif C[0] == "deck":      
        if C[1] == "add":
            if (C[2][0] in "AKQJT98765432") and (C[3][0] in "SHCD") and (C[4] in enhancementlist) and (C[5] in editionlist) and (C[6] in seallist):
                deck.append([C[2], C[3], C[4], C[5], C[6]])
                if C[4] == "unenh":
                    enh = ""
                else:
                    enh = C[4]+" "
                if C[5] == "base":
                    e = ""
                else:
                    e = C[5]+" "
                if C[6] == "Noseal":
                    s = ""
                else:
                    s = C[6]+" Seal "
                print("Added a", e+s+enh+C[2]+" of "+C[3], "to deck\n")
            else:
                print("""Invalid card. Syntax: deck add [rank: A/K/Q/J/T/9/8/7/6/5/4/3/2] [suit: S/H/C/D] [enhancement: unenh/bonus/mult/wild/glass/steel/stone/gold/lucky]
[edition: base/foil/holo/poly/neg] [seal: Noseal/Gold/Red/Blue/Purple]\n""")
        elif C[1] == "remove":
            if [C[2], C[3], C[4], C[5], C[6]] in deck:
                deck.remove([C[2], C[3], C[4], C[5], C[6]])
                if C[4] == "unenh":
                    enh = ""
                else:
                    enh = C[4]+" "
                if C[5] == "base":
                    e = ""
                else:
                    e = C[5]+" "
                if C[6] == "Noseal":
                    s = ""
                else:
                    s = C[6]+" Seal "
                print("Removed a", e+s+enh+C[2]+" of "+C[3], "from the deck\n")
            else:
                print("Could not locate this card\n")
        elif C[1] == "default":
            deck = list(deckdefault); print("Deck has been set to default\n")
        elif C[1] == "clear":
            deck = []; print("Deck has been cleared\n")
        elif C[1] == "type":
            if C[2] in decklist:
                decktype = C[2]; print("Deck type has been changed to", C[2]+"\n")
        elif C[1] == "list":
            print(decktype, "Deck:")
            for card in deck:
                if card[2] == "unenh":
                    enh = ""
                else:
                    enh = card[2]+" "
                if card[3] == "base":
                    e = ""
                else:
                    e = card[3]+" "
                if card[4] == "Noseal":
                    s = ""
                else:
                    s = card[4]+" Seal "
                print(e+s+enh+card[0]+" of "+card[1])
            print()
        else:
            print("""Invalid command. Try deck add [rank: A/K/Q/J/T/9/8/7/6/5/4/3/2] [suit: S/H/C/D] [enhancement: unenh/bonus/mult/wild/glass/steel/stone/gold/lucky]
[edition: base/foil/holo/poly/neg] [seal: Noseal/Gold/Red/Blue/Purple], deck remove [rank: A/K/Q/J/T/9/8/7/6/5/4/3/2] [suit: S/H/C/D]
[enhancement: unenh/bonus/mult/wild/glass/steel/stone/gold/lucky] [edition: base/foil/holo/poly/neg] [seal: Noseal/Gold/Red/Blue/Purple], deck clear, deck default,
deck type [type: Red/Blue/Yellow/Green/Black/Magic/Nebula/Ghost/Abandoned/Checkered/Zodiac/Painted/Anaglyph/Plasma/Erratic/Challenge], or deck list.\n""")
    elif C[0] == "list":
        if C[1] == "jokers":
            print("All jokers:\n"+", ".join(jokerlist))
            print("""\nNote that in the game\'s code:
- Canio is referred to as \"caino\"
- Ceremonial Dagger is referred to as \"ceremonial\"
- Delayed Gratification is referred to as \"delayed_grat\"
- Driver's License is referred to as \"drivers_license\"
- Golden Ticket is referred to as \"ticket\"
- Mail-in Rebate is referred to as \"mail\"
- Oops All 6s is referred to as \"oops\"
- Seltzer is referred to as \"selzer\"
- Showman is referred to as \"ring_master\"
- Smiley Face is referred to as \"smiley\"
  - Spare Trousers is referred to as \"trousers\"
- To Do List is referred to as \"todo_list\"
- The word "card" is missing from Baseball Card, Flash Card, Gift Card, and Trading Card 
- The word "the" is missing from The Idol, The Duo, The Trio, The Family, The Order, and The Tribe 
- Apart from Joker, Greedy Joker, Lusty Joker, Wrathful Joker, Gluttonous Joker, Blue Joker, and Green Joker, the word "joker" is missing from all other jokers containing the word "Joker"\n""") 
        elif C[1] == "tarots":
            print("All tarots: "+", ".join(tarotlist))
            print("""\nNote that in the game\'s code:
- The Hierophant is referred to as \"heirophant\"
- Temperance is referred to as \"temperence\"
- The word "the" is missing from all tarot cards containing the word "The"\n""")
        elif C[1] == "planets":
            print("All planets: "+", ".join(planetlist)+"\n")
        elif C[1] == "spectrals":
            print("All spectrals: "+", ".join(spectrallist)+"\n")
            print("\nNote that in the game's code, The Soul is referred to as \"soul\"\n")
        elif C[1] == "vouchers":
            print("All vouchers: "+", ".join(voucherlist)+"\n")
            print("""\nNote that in the game\'s code:
- Director's Cut is referred to as \"directors_cut\"
- Overstock is referred to as \"overstock_norm\"
- Reroll Glut and Reroll Surplus are missing from the list since they can cause a crash\n""")
        elif C[1] == "packs":
            print("All packs: "+", ".join(packlist)+"\n")
        elif C[1] == "tags":
            print("All tags: "+", ".join(taglist)+"\n")
            print("""\nNote that in the game\'s code:
- D6 Tag is referred to as \"d_six\"
- Speed Tag is referred to as \"skip\"\n""")
        elif C[1] == "blinds":
            print("All blinds: "+", ".join(blindlist)+"\n")
        else:
            print("Invalid command. Try list [jokers/tarots/planets/spectrals/vouchers/packs/tags/blinds]\n")
    elif C[0] == "modifier":
        if C[1] == "joker_slots":
            modifiers[0][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "consumable_slots":
            modifiers[1][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "hand_size":
            modifiers[2][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "hands":
            modifiers[3][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "discards":
            modifiers[4][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "dollars":
            modifiers[5][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "reroll_cost":
            modifiers[6][1] = C[2]; print("Modifier", C[1], "has been set to", C[2]+"\n")
        elif C[1] == "default":
            modifiers = list(modifiersdefault); print("Modifiers have been set to their default values\n")
        elif C[1] == "list":
            for modifier in modifiers:
                print(modifier[0]+": "+modifier[1])
            print()
        else:
            print("Invalid command. Try modifier [modifier: joker_slots/hand_size/consumable_slots/hands/discards/dollars/reroll_cost] [value], modifier default or modifier list.\n")
    elif C[0] == "customrules":
        if (C[1] == "add") and (C[2] in customruleslist):
            if C[2] in customrules:
                print(C[2], "is already active\n")
            else:
                customrules.append(C[2]); print("Added", C[2], "to custom rules\n")
        elif C[1] == "remove":
            if C[2] in customrules:
                customrules.remove(C[2]); print("Removed", C[2], "from custom rules\n")
            else:
                print("Could not locate custom rule\n")
        elif C[1] == "list":
            print("Custom rules:", ", ".join(customrules)+"\n")
        else:
            print("Invalid command. Try customrules add [customrule], customrules remove [customrule], or customrules list.\n")
    elif C[0] == "header":
        if C[1] == "name":
            header[0] = C[2]; print("mod_name has been set to", C[2]+"\n")
        elif C[1] == "id":
            header[1] = C[2]; print("mod_id has been set to", C[2]+"\n")
        elif C[1] == "author":
            header[2] = C[2]; print("mod_author has been set to", C[2]+"\n")
        elif C[1] == "description":
            header[3] = C[2]; print("mod_description has been set to", C[2]+"\n")
        elif C[1] == "list":
            print("--- STEAMMODDED HEADER\n--- MOD_NAME: "+header[0]+"\n--- MOD_ID: "+header[1]+"\n--- MOD_AUTHOR: "+header[2]+"\n--- MOD_DESCRIPTION: "+header[3]+"\n")
        else:
            print("Invalid command. Try header name [name], header id [id], header author [author], header description [description], or header list.\n")
    elif C[0] == "print":
        printmod(header, customrules, modifiers, jokers, consumables, vouchers, deck, decktype, bannedjokers, bannedconsumables, bannedvouchers, bannedpacks, bannedtags, bannedblinds)
    elif C[0] == "export":
        export(header, customrules, modifiers, jokers, consumables, vouchers, deck, decktype, bannedjokers, bannedconsumables, bannedvouchers, bannedpacks, bannedtags, bannedblinds)
        print("Export file", header[0]+".lua complete\n")
    else:
        print("Invalid command. Type in the command help for a list of all commands.\n")
            












        
