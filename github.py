# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

import requests

from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text


@friday_on_cmd(
    ["github"],
    cmd_help={
        "help": "Get information about an user on GitHub.",
        "example": "{ch}github username_github",
    },
)
async def github_(client,message):
    msg = await edit_or_reply(message, "`Processing!`")
    text = get_text(message)
    if not text:
        await editer.edit("`Please Enter Valid Input`")
        return
    url = "https://api.github.com/users/{}".format(text)
    r = requests.get(url)
    if r.status_code != 404:
        b = r.json()
        avatar_url = b.get("avatar_url")
        html_url = b.get("html_url")
        gh_type = b.get("type")
        name = b.get("name")
        company = b.get("company")
        blog = b.get("blog")
        location = b.get("location")
        bio = b.get("bio")
        created_at = b.get("created_at")
        cap = f"`Name`: [{name}]({html_url})\n`Type`: **{gh_type}**\n`Company`**: {company}**\n`Blog`: **{blog}**\n`Location`: **{location}**\n`Bio`: **{bio}**\n`Profile Created`:** {created_at}**"
        if avatar_url:
            await msg.delete()
            await client.send_photo(message.chat.id, avatar_url, caption=cap)
        else:
            await msg.edit(cap)
    else:
        await msg.edit(f"`404 : UserNot Found!`")
