import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def team(ctx, num1: int, num2: int, num3: int, num4: int, num5: int, num6: int):
    # Check if single digit numbers are between 1 and 7
    if 1 <= num2 <= 7 and 1 <= num4 <= 7 and 1 <= num6 <= 7:
        # Image URLs to be updated as per your requirement
        image_urls = [
            "https://example.com/image1.png",
            "https://example.com/image2.png",
            "https://example.com/image3.png",
            "https://example.com/image4.png",
            "https://example.com/image5.png",
            "https://example.com/image6.png",
            "https://example.com/image7.png",
        ]

        # Build the image URLs based on user input
        image_urls[num2 - 1] += str(num1) + ".png"
        image_urls[num4 - 1] += str(num3) + ".png"
        image_urls[num6 - 1] += str(num5) + ".png"

        # Create an embed with images in the specified positions
        embed = discord.Embed(title="Team Configuration", color=0x00ff00)
        embed.set_image(url=image_urls[0])
        embed.add_field(name="Position 1", value=f"Image {num2}", inline=True)
        embed.set_image(url=image_urls[1])
        embed.add_field(name="Position 2", value=f"Image {num4}", inline=True)
        embed.set_image(url=image_urls[2])
        embed.add_field(name="Position 3", value=f"Image {num6}", inline=True)

        await ctx.send(embed=embed)
    else:
        await ctx.send("Invalid position numbers. Please use numbers between 1 and 7.")

# Run the bot with your token
bot.run(MTE5ODA3MjQ5NjI4MTM3NDczMA.GA4LEf.xOxw-lZN67OtrD0v8t40awKybkLWgztoYWF9mo)
