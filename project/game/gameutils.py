#need to update everything once i get the user authen

from .models import Gamesumm, playerData
from asgiref.sync import sync_to_async

async def GaneSumm(game):
    try:
        summary = await sync_to_async(Gamesumm.objects.create)(
            gametype = game.gametype,
            redteam_Score = game.redscore,
            blueteam_Score = game.bluescore,
        )
        for player in game.redteamplayers:
            player_obj = await sync_to_async(playerData.objects.get)(id=player.id)
            await sync_to_async(summary.redteam_players.add)(player_obj)

        for player in game.blueteamplayers:
            player_obj = await sync_to_async(playerData.objects.get)(id=player.id)
            await sync_to_async(summary.blueteamp_players.add)(player_obj)

        # for player in summary.red

        await sync_to_async(summary.save)()

    except Exception as e:
        print (f'Error new sum: {e}')