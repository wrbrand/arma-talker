# based on Arma2 voice commands script by Suchy

# Keys in SUBJECTS can have no more than 2 words # TODO: Enforce
# All items in the value lists must be keys of pydirectinput.KEYBOARD_MAPPING # TODO: Enforce
SUBJECTS: dict[str, list[str]] = {
    "all": ["`"],
    "i\'ll": ["`"],
    "everyone": ["`"],
    "everybody": ["`"],
    "squad": ["`"],
    "2": ["f2"],
    "to": ["f2"],
    "number two": ["f2"],
    "3": ["f3"],
    "three": ["f3"],
    "number three": ["f3"],
    "or": ["f4"],
    "4": ["f4"],
    "for": ["f4"],
    "four": ["f4"],
    "number four": ["f4"],
    "5": ["f5"],
    "five": ["f5"],
    "number five": ["f5"],
    "6": ["f6"],
    "sex": ["f6"],
    "number six": ["f6"],
    "number sex": ["f6"],
    "7": ["f7"],
    "number seven": ["f7"],
    "8": ["f8"],
    "number eight": ["f8"],
    "9": ["f9"],
    "number nine": ["f9"],
    "10": ["f10"],
    "number 10": ["f10"],
    "11": ["f12", "f1", "f11"],
    "number 11": ["f12", "f1", "f11"],
    "12": ["f12", "f2", "f11"],
    "number 12": ["f12", "f2", "f11"],
    "13": ["f12", "f3", "f11"],
    "number 13": ["f12", "f3", "f11"],

    # Teams
    "red": ["backspace", "backspace", "9", "9", "1"],
    "team red": ["backspace", "9", "9", "1"],
    "red team": ["backspace", "9", "9", "1"],
    "green": ["backspace", "9", "9", "2"],
    "team green": ["backspace", "9", "9", "2"],
    "green team": ["backspace", "9", "9", "2"],
    "blue": ["backspace", "9", "9", "3"],
    "team blue": ["backspace", "9", "9", "3"],
    "blue team": ["backspace", "9", "9", "3"],
    "yellow": ["backspace", "9", "9", "4"],
    "team yellow": ["backspace", "9", "9", "4"],
    "yellow team": ["backspace", "9", "9", "4"],
    "white": ["backspace", "9", "9", "5"],
    "team white": ["backspace", "9", "9", "5"],
    "white team": ["backspace", "9", "9", "5"],
}

COMMANDS: dict[str, list[str]] = {
    "go there": [" "],
    "go here": [" "],
    "move there": [" "],
    "move here": [" "],
    "move up": [" "],
    "take that position": [" "],
    "go over there": [" "],
    "go over here": [" "],
    # "go to that": [" "], # TODO
    # "go to the": [" "], # TODO

    "target that": ["enter"],
    "attack that": ["enter"],
    "attack here": ["enter"],
    "watch there": ["enter"],
    "watch that": ["enter"],
    "watch here": ["enter"],

    "open fire": ["3", "1"],
    "clear to engage": ["3", "1"],
    "free to engage": ["3", "1"],
    "weapons hot": ["3", "1"],
    "weapons free": ["3", "1"],
    "fire at will": ["3", "1"],
    "hold fire": ["3", "2"],
    "hold your fire": ["3", "2"],
    "ceasefire": ["3", "2"],
    "cease fire": ["3", "2"],
    "don't shoot": ["3", "2"],
    "stop shooting": ["3", "2"],
    "fire": ["3", "3"],
    "shoot": ["3", "3"],
    "engage": ["3", "4"],
    "engage at will": ["3", "5"],
    "disengage": ["3", "6"],
    "scan horizon": ["3", "7"],
    "scan the horizon": ["3", "7"],
    "look around": ["3", "7"],

    "watch north": ["3", "8", "1"],
    "watch northeast": ["3", "8", "2"],
    "watch east": ["3", "8", "3"],
    "watch southeast": ["3", "8", "4"],
    "watch south": ["3", "8", "5"],
    "watch southwest": ["3", "8", "6"],
    "watch west": ["3", "8", "7"],
    "watch northwest": ["3", "8", "8"],

    "suppressive fire": ["3", "9"],
    "suppressing fire": ["3", "9"],
    "lay down some fire": ["3", "9"],
    "give me a base of fire": ["3", "9"],
    "and its suppressing fire": ["3", "9"],
    "and its suppressive fire": ["3", "9"],
    "i need suppressive fire": ["3", "9"],
    "i need suppressing fire": ["3", "9"],

    # Reports
    "report status": ["5", "5"],
    "report in": ["5", "5"],
    "status": ["5", "5"],
    "location": ["5", "5"],
    "what\'s your location": ["5", "5"],
    "position": ["5", "5"],
    "what\'s your position": ["5", "5"],
    "coordinates": ["5", "5"],
    "send coordinates": ["5", "5"],
    "send sitrep": ["5", "5"],
    "sitrep": ["5", "5"],
    "what\'s your status": ["5", "5"],
    "where are you": ["5", "5"],
    "status report": ["5", "5"],
    "give me a status report": ["5", "5"],
    "do you read": ["5", "5"],

    "taking fire": ["backspace", "5", "6"],
    "under fire": ["backspace", "5", "6"],
    "help me out": ["backspace", "5", "6"],
    "give me a hand": ["backspace", "5", "6"],
    "i could use some help": ["backspace", "5", "6"],
    "i\'m under fire": ["backspace", "5", "6"],

    "enemy down": ["backspace", "5", "7"],
    "he\'s down": ["backspace", "5", "7"],
    "he\'s history": ["backspace", "5", "7"],
    "soldier is history": ["backspace", "5", "7"],
    "scratch one": ["backspace", "5", "7"],
    "tango down": ["backspace", "5", "7"],
    "hostile down": ["backspace", "5", "7"],
    "target destroyed": ["backspace", "5", "7"],
    "target neutralized": ["backspace", "5", "7"],
    "target eliminated": ["backspace", "5", "7"],
    "hostile eliminated": ["backspace", "5", "7"],

    "is down": ["backspace", "5", "8"],
    "are down": ["backspace", "5", "8"],

    "report targets": ["backspace", "5", "9"],
    "report enemies": ["backspace", "5", "9"],
    "do you see anything": ["backspace", "5", "9"],
    "what do you see": ["backspace", "5", "9"],

    # Combat mode
    "stealth": ["7", "1"],
    "be quiet": ["7", "1"],
    "keep quiet": ["7", "1"],

    "danger": ["7", "2"],
    "get ready to fight": ["7", "2"],
    "get ready for combat": ["7", "2"],

    "be alert": ["7", "3"],
    "be aware": ["7", "3"],
    "stay alert": ["7", "3"],
    "stay aware": ["7", "3"],
    "stay frosty": ["7", "3"],
    "watch out": ["7", "2"],

    "at ease": ["7", "4"],
    "safe": ["7", "4"],
    "it's safe": ["7", "4"],

    "get up": ["7", "6"],
    "stand up": ["7", "6"],
    "up and adam": ["7", "6"],
    "on your feet": ["7", "6"],

    "crouch": ["7", "7"],
    "stay crouched": ["7", "7"],
    "heads low": ["7", "7"],

    "get down": ["7", "8"],
    "go prone": ["7", "8"],
    "hit the dirt": ["7", "8"],
    "on the ground": ["7", "8"],

    "keep low": ["7", "9"],
    "copy my stance": ["7", "9"],
    "follow my lead": ["7", "9"],

    # Reply
    "done": ["backspace", "0", "1"],
    "i\'m done": ["backspace", "0", "1"],
    "waiting for orders": ["backspace", "0", "1"],
    "waiting": ["backspace", "0", "1"],
    "i\'m waiting": ["backspace", "0", "1"],
    "ready": ["backspace", "0", "1"],
    "i\'m ready": ["backspace", "0", "1"],
    "ready and waiting": ["backspace", "0", "1"],
    "negative": ["backspace", "0", "2"],
    "sorry can\'t do that": ["backspace", "0", "2"],
    "sorry no can do": ["backspace", "0", "2"],
    "can\'t do that": ["backspace", "0", "2"],
    "can\'t do it": ["backspace", "0", "2"],
    "no can do": ["backspace", "0", "2"],

    "ready to fire": ["backspace", "0", "3"],
    "eyes on target": ["backspace", "0", "3"],
    "target in sight": ["backspace", "0", "3"],
    "target inside": ["backspace", "0", "3"],
    "turn it inside": ["backspace", "0", "3"],

    "cannot fire": ["backspace", "0", "4"],
    "can\'t see the target": ["backspace", "0", "4"],
    "i can\'t see the target": ["backspace", "0", "4"],
    "i don\'t see the target": ["backspace", "0", "4"],
    "no line of fire": ["backspace", "0", "4"],

    "repeat last": ["backspace", "0", "6"],
    "repeat": ["backspace", "0", "6"],
    "say again over": ["backspace", "0", "6"],
    "say again": ["backspace", "0", "6"],
    "didn\'t copy": ["backspace", "0", "6"],

    # Formation
    "stay in formation": ["1", "1"],
    "stay close": ["1", "1"],
    "stick close": ["1", "1"],
    "keep formation": ["1", "1"],
    "return to formation": ["1", "1"],
    "back to formation": ["1", "1"],
    "regroup": ["1", "1"],
    "follow me": ["1", "1"],
    "get back": ["1", "1"],
    "get back here": ["1", "1"],
    "fall back": ["1", "1"],
    "fall back to formation": ["1", "1"],
    "fall back into formation": ["1", "1"],
    "form up": ["1", "1"],
    "return": ["1", "1"],
    "form on me": ["1", "1"],

    "advance": ["1", "2"],
    "take point": ["1", "2"],
    "you take point": ["1", "2"],

    "push up": ["1", "3"],
    "stay back": ["1", "3"],
    "go back": ["1", "3"],
    "stay behind": ["1", "3"],
    "keep the distance": ["1", "3"],
    "keep a distance": ["1", "3"],
    "keep back": ["1", "3"],
    "keep behind": ["1", "3"],

    "flank left": ["1", "4"],
    "take the left flank": ["1", "4"],
    "flank right": ["1", "5"],
    "take the right flank": ["1", "5"],

    "stop": ["1", "6"],
    "halt": ["1", "6"],
    "stay here": ["1", "6"],
    "don\'t move": ["1", "6"],
    "stop where you are": ["1", "6"],
    "stay where you are": ["1", "6"],
    "stay there": ["1", "6"],
    "stop there": ["1", "6"],

    "wait": ["1", "7"],
    "wait for me": ["1", "7"],
    "hold on": ["1", "7"],
    "let me catch up": ["1", "7"],

    "find cover": ["1", "8"],
    "find some cover": ["1", "8"],
    "get to cover": ["1", "8"],
    "take cover": ["1", "8"],

    "next waypoint": ["1", "9"],
    "head to next waypoint": ["1", "9"],
    "head to the next waypoint": ["1", "9"],
    "move to next waypoint": ["1", "9"],
    "move to the next waypoint": ["1", "9"],
    "go to next waypoint": ["1", "9"],
    "go to the next waypoint": ["1", "9"],
    "proceed to next waypoint": ["1", "9"],
    "proceed to the next waypoint": ["1", "9"],

     # Teams
    "assign red": ["9", "1"],
    "your red": ["9", "1"],
    "your team red": ["9", "1"],
    "your red team": ["9", "1"],
    "you\'re red": ["9", "1"],
    "you\'re team red": ["9", "1"],
    "you\'re red team": ["9", "1"],

    "assign green": ["9", "2"],
    "your green": ["9", "2"],
    "your team green": ["9", "2"],
    "your green team": ["9", "2"],
    "you\'re green": ["9", "2"],
    "you\'re team green": ["9", "2"],
    "you\'re green team": ["9", "2"],

    "assign blue": ["9", "3"],
    "your blue": ["9", "3"],
    "your team blue": ["9", "3"],
    "your blue team": ["9", "3"],
    "you\'re blue": ["9", "3"],
    "you\'re team blue": ["9", "3"],
    "you\'re blue team": ["9", "3"],

    "assign yellow": ["9", "4"],
    "your yellow": ["9", "4"],
    "your team yellow": ["9", "4"],
    "your yellow team": ["9", "4"],
    "you\'re yellow": ["9", "4"],
    "you\'re team yellow": ["9", "4"],
    "you\'re yellow team": ["9", "4"],

    "assign white": ["9", "5"],
    "your white": ["9", "5"],
    "your team white": ["9", "5"],
    "your white team": ["9", "5"],
    "you\'re white": ["9", "5"],
    "you\'re team white": ["9", "5"],
    "you\'re white team": ["9", "5"],
}

# //Mount
# key.enter=said("get inside that",1)
# key.enter=said("get in that",1)
# key.enter=said("board that",1)
# key.enter=said("mount that",1)
#
# key.4,key.2,key.1=said("get inside",5)
# key.4,key.2,key.1=said("get in",5)
#
#
# key.4,key.2,key.2=said("you're driver")
# key.4,key.2,key.2=said("you drive")
# key.4,key.2,key.2=said("you're driving")
# key.4,key.2,key.2=said("take driver position")
# key.4,key.2,key.2=said("take driver seat")
# key.4,key.2,key.2=said("grab the wheel")
# key.4,key.2,key.2=said("driver get in")
# key.4,key.2,key.2=said("driver",5)
# key.4,key.2,key.2=said("you're pilot")
# key.4,key.2,key.2=said("take pilot position")
# key.4,key.2,key.2=said("take pilot seat")
# key.4,key.2,key.2=said("grab the stick")
# key.4,key.2,key.2=said("pilot get in")
# key.4,key.2,key.2=said("pilot",5)
#
# key.4,key.2,key.4=said("you're gunner")
# key.4,key.2,key.4=said("take gunner position")
# key.4,key.2,key.4=said("get on the gun")
# key.4,key.2,key.4=said("take the gun")
# key.4,key.2,key.4=said("mount the gun")
# key.4,key.2,key.4=said("gunner get in")
# key.4,key.2,key.4=said("gunner",5)
#
# key.4,key.1=said("disembark")
# key.4,key.1=said("dismount")
# key.4,key.1=said("get out")
# key.4,key.1=said("out of the vehicle")
# key.4,key.1=said("get out of the vehicle")
#
# //Status
# key.5,key.1,key.1=said("Requesting medic support")
# key.5,key.1,key.1=said("Request medic support")
# key.5,key.1,key.1=said("Requesting medical support")
# key.5,key.1,key.1=said("Request medical support")
# key.5,key.1,key.2=said("Requesting ambulance")
# key.5,key.1,key.2=said("Requesting ambulance support")
# key.5,key.1,key.2=said("Request ambulance")
# key.5,key.1,key.3=said("Requesting repair truck")
# key.5,key.1,key.3=said("Requesting repair")
# key.5,key.1,key.4=said("Requesting ammo support")
# key.5,key.1,key.4=said("Requesting ammunition support")
# key.5,key.1,key.4=said("Requesting ammo")
# key.5,key.1,key.5=said("Requesting ammunition")
# key.5,key.1,key.5=said("Requesting fuel support")
# key.5,key.1,key.5=said("Requesting fuel truck")
#
# key.5,key.2=said("Fuel low") or said("I'm out of fuel") or said ("Out of fuel")
# key.5,key.3=said("Ammo low") or said("I need ammo") or said ("I need ammunition")
# key.5,key.4=said("Injuried") or said("I need medic") or said ("Medic")
# key.5,key.4=said("I'm wounded") or said("I'm hit") or said ("I've been hit")
#

#
#
# //Action (unfortunately it's mostly context)
# key.6,key.1=said("heal",3) or said("heal me") or said("heal him") or said("heal that",1)
# key.6=said("action")
# key.1=said("option 1")
# key.2=said("option 2")
# key.3=said("option 3")
# key.4=said("option 4")
# key.5=said("option 5")
# key.6=said("option 6")
# key.7=said("option 7")
# key.8=said("option 8")
# key.9=said("option 9")
# key.0=said("option 0")
#
#
# //Formation
# key.8,key.1=said("give me a column") or said("form column") or said("formation column")
# key.8,key.2=said("give me a staggered column") or said("form staggered column") or said("formation staggered column")
# key.8,key.2=said("give me a double column") or said("form double column") or said("formation double column")
# key.8,key.3=said("give me a wedge") or said("form wedge") or said("formation wedge")
# key.8,key.4=said("give me an echelon left") or said("form echelon left") or said("formation echelon left")
# key.8,key.5=said("give me an echelon right") or said("form echelon right") or said("formation echelon right")
# key.8,key.6=said("give me a V") or said("form V") or said("formation V")
# key.8,key.7=said("give me a line") or said("form line") or said("formation line")
# key.8,key.8=said("give me a compact column") or said("form compact column") or said("formation compact column")
# key.8,key.8=said("give me a compact") or said("form compact") or said("formation compact") or said("form file") or said ("formation file")
# key.8,key.9=said("give me a delta") or said("form delta") or said("formation delta")
# key.8,key.9=said("give me a diamond") or said("form diamond") or said("formation diamond")
#
