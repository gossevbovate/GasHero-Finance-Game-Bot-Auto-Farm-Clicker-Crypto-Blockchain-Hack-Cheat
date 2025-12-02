from streamlit import secrets

twitter_icon = '[![Repo](https://img.icons8.com/color/48/000000/twitter--v1.png)](https://twitter.com/Ninja76224909)'

HEROS = ["iron lady", "ape commander", "biorobotic soldier", "black sapphire", "space captain", "spore lord", "ruthless warden", "guardian angel", "combat queen", "lone werewolf", "the trailblazer", "nano swamp", "the yokozuna", "ascetic monk", "tactical police", "blessed kid", "junior shifu", "deadly nightshade", "meditating master", "unstoppable force", "amazon warrior", "blackmarket baroness", "red mercury", "nuclear martyr", "swift blade", "loan shark", "altruistic banker", "devil's follower", "decommissioned unit", "death's hand", "professor dark matter", "lil' bulldozer", "artificial empathy", "praying nun", "arctic sheriff", "high priestess", "truth seeker", "faith healer", "street musician", "media tycoon", "the godfather", "leader of the pack", "historical linguist", "tech tinker", "rocket scientist", "telekinetic woman", "charming attorney", "field medic"]
HEROS.sort()
HEROS = ['']+HEROS

WEAPONS = ('', 'dagger', 'sword', 'axe', 'hammer', 'bow', 'gun', 'staff', 'book',)

PETS = ('', 'dragon', 'treant', 'crab', 'panda',)

mongo_srv_url = secrets["mongo_srv_url"]

