#!/bin/python3
import discord
from discord import Status
import asyncio
from vesync.api import VesyncApi,


discordUser = "DISCORD USERNAME GOES HERE"
outletid = "OUTLET ID GOES HERE"

class Outlet:
    api = VesyncApi("username", "password")

    def get_device_status(id):
        info = Outlet.api.get_devices()
        for outlet in info:
            if outlet["cid"] == id:
                return outlet["deviceStatus"]

    def toggle_device(id):
        status = Outlet.get_device_status(id)
        if status == "off":
            Outlet.api.turn_on(id)
        if status == "on":
            Outlet.api.turn_off(id)


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.user.bot)
    print('------')

@client.event
async def on_member_update(before, after):
    if str(before.status) == "online":
        if str(after.status) != "online":
            if str(after.name) == discordUser:
                print("{} has gone {}.".format(after.name,after.status))
                Outlet.api.turn_off(outletid)
            
    if str(before.status) != "online":
        if str(after.status) == "online":
            if str(after.name) == discordUser:
                print("{} has gone {}.".format(after.name,after.status))
                Outlet.api.turn_on(outletid)
    

client.run('DISCORD TOKEN GOES HERE')