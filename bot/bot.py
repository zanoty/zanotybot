from sc2.bot_ai import BotAI, Race
from sc2.data import Result
from sc2.ids.ability_id import AbilityId

class CompetitiveBot(BotAI):
    NAME: str = "ZanotyBot"
    """This bot's name"""

    RACE: Race = Race.Zerg
    """This bot's Starcraft 2 race.
    Options are:
        Race.Terran
        Race.Zerg
        Race.Protoss
        Race.Random
    """

    async def on_start(self):
        """
        This code runs once at the start of the game
        Do things here before the game starts
        """
        print("Game started")

    async def on_step(self, iteration: int):
        """
        This code runs continually throughout the game
        Populate this function with whatever your bot should do!
        """
       #make Drone if we have minerals and supply is ok
        if self.can_afford("Drone") and self.supply_left > 0 and self.larva > 0:
            my_larva = self.larva.random
            my_larva(AbilityID.Larvation_Drone)
        pass

    async def on_end(self, result: Result):
        """
        This code runs once at the end of the game
        Do things here after the game ends
        """
        print("Game ended.")
