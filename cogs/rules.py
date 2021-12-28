import discord
from discord.ext import commands


class Rules(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rulez1(self, ctx):
        embed = discord.Embed(
        title = "**TEXT CHANNEL RULES - PAGE  1**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  Respect Every Single Member In The Server In Simple Words Give Respect Take Respect.\n\n<:dhrules:911452181553610802>  ld Sever Members Are Supposed To Welcome New Members In A Polite Manner And Keep Them Engaged In Your Conversations As Much Possible, Don't Behave Harshly With New Members Since They Aren't Enough Familiar With Discord Or Server's Environment.\n\n<:dhrules:911452181553610802>  Spamming,Harassment,Abuse,Hate Speech Or Any Kind Of Toxic Behavior Will Not Be Tolerated.\n\n<:dhrules:911452181553610802>   Text Walls Or A large Paragraphs Of Text Aren't Allowed. It Is Allowed Only In Discord Promotion Channel.\n\n<:dhrules:911452181553610802>  Don't Tag Owner i.e. Dude Hunter Frequently And Unnecessarily You'll Receive Warnings From Moderators For That.\n\n<:dhrules:911452181553610802>   Hating/Racist/Regional/Religious/Personal Abusing Comments Aren't Allowed. Just Respect Everyone Else,Friendly Arguments Are Ok Upto Certain Limits.\n\n<:dhrules:911452181553610802>   User Accounts Impersonating Dude Hunter ( i.e. Using Dude Hunter's  Name/His Profile Picture) Are Supposed To Change Their Usernames/Profile Pictures As Soon As Possible After Joining Server Also If Already In The Server Otherwise Those Accounts Will Be Kicked Or Banned From The Sever.\n\n<:dhrules:911452181553610802>   Impersonating Any Of Server Members/Moderation/Management Teams And Owner Is Strictly Prohibited And Will Lead To Administrative Actions Immediately.\n\n<:dhrules:911452181553610802>  Female Members Of The Server Are Supposed To Verify Themselves Through Voice Channels Before Being Moderators.  As Soon As Possible Upon Joining Server Also If Already In Server To Avoid Certain Scenarios, Impersonating Using Fake Female Accounts Will Get Permanent Server Ban Once Proven.\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def rulez2(self, ctx):
        embed = discord.Embed(
        title = "**TEXT CHANNEL RULES - PAGE 2**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  Backseat/Mini Moderation Isn't Allowed. (Helping New Members Upto Some Aspects Is Nice Thing But Doing Mini Moderation Like Warning/Scolding Someone In Presence Even In Absence Of Management/Moderators Isn't Allowed)\n\n<:dhrules:911452181553610802>  Adult (18+), Explicit, NSFW Content Including Profile Pics, Gif,Images,Text,Nicknames Etc. Aren't Allowed Also Keeping Bot Names Or Bot Profile Pictures Is Strictly Prohibited.\n\n<:dhrules:911452181553610802>  Asking For Private Information Isn't Allowed In Chat Also Revealing Private Information About Any Of Server Members Is Zero Tolerance Rule.\n\n<:dhrules:911452181553610802>  You're Supposed To Use Fun-Bots (Casino/Pokécord/Dank Memer etc) At Fun Basis, Arguing/Abusing Someone Upon Fun-Bots Activities Isn't Allowed For Eg. Robbing Money From Casino (It's Your Own Responsibility To Deposit Your Money In The Bank), Catching Pokémon, Dueling, Trading, Battling (You Should Be Quick Enough Than Other Member While Catching Pokémon, Rest Commands Should Be Taken As A Fun Purpose Only), Roasting, Fun Commands Used Upon You Or Robbing Money In Dank-memer. (It's For Fun Don't Take It Seriously And You Should Deposit Earned Coins Routinely In Your Bank)\n\n<:dhrules:911452181553610802>  While Listening Songs You're Supposed To Respect Others Members Song Choice, Skipping Songs Multiple Times Solely Without Using Vote-Skip Feature Isn't Welcomed Either You Can Use Another Music Bot and Another Songs VC Or Wait Till Your Song Comes.\n\n<:dhrules:911452181553610802>  Playing NSFW/18+/Abusive/Explicit Songs (Running Commands In Text Channels And Listening In Voice Channels) Isn't Allowed And Will Lead To Administrative Actions Accordingly.\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def rulez3(self, ctx):
        embed = discord.Embed(
        title = "**TEXT CHANNEL RULES - PAGE 3**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  Anyone Found With Alternative Accounts Will Get All The Alternatives As Well As Main Account Permanently Banned From Sever, If You Have Any Prior Reason For Keeping Alternative Id In Server You've To Talk With Management Before Doing Such For Their Permission.\n\n<:dhrules:911452181553610802>  Raiding Discord Server Through Bot Accounts Or Manually Through Provoking Human Accounts Is Against Discord's TOS/Guidelines, Raiders Will Get Permanent Server Ban As Well As Information About Such Raid Will Be Forwarded Immediately To Discord Officials For Further Investigation/Actions.\n\n<:dhrules:911452181553610802>  Every Member Is Supposed To Read And Follow Discord TOS And Guidelines.\n\n<:Invite:898601220502081556>  Discord TOS :- https://discord.com/terms\n\n<:Invite:898601220502081556>  Community Guidelines :- https://discord.com/guidelines\n\n<:dhrules:911452181553610802>  Black Stripped Text, Spoilers, Zalgo Text, Regional Language Typography Is Not Allowed. You're Supposed To Use Standard English Typography. Spoilers Are Allowed Only In A Limit.\n\n<:dhrules:911452181553610802>  Talking About Topics Related To Religion/Politics/Any Single Topic That Will Initiate Controversy As Well As About Other Streamers/Discord Servers Isn't Allowed.\n\n<:dhrules:911452181553610802>   Advertising Of Youtube Channels/Other Platforms/Discord Servers Isn't Allowed\n\n<:dhrules:911452181553610802>  Self Promoting Your Own Content Such As Links,Videos Or Photos Is Allowed Only  in 😜<#894227446369513492>  and 😜<#896405199697108992> \n\n<:dhrules:911452181553610802>  Don't Spam Emojis/Same Words/Phrases And Sentences Unnecessarily In General Or Any Other Text Channels, It Won't Help You To Gain Experience(Xp) Level Up Anymore.\n\n<:dhrules:911452181553610802>  Inviting Unofficial Bots Isn't Allowed.\n\n<:dhrules:911452181553610802>  Do Not Perform Or Promote Intentional Use Of In Game Glitches, Hacks Or Bugs\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green(),
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def rulez4(self, ctx):
        embed = discord.Embed(
        title = "**TEXT CHANNEL RULES - PAGE 4**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>   Do Not Mention @everyone Or @here Tags.\n\n<:dhrules:911452181553610802>   If Administration/Management/Moderator Are Asking To Change The Topic Then It Should Be Changed Regardless Of Any Arguments.\n\n<:dhrules:911452181553610802>  Don't Argue With Administration/Management/Moderators Unnecessarily In Chat, Their Decisions Will Be Last Decisions.\n\n<:dhrules:911452181553610802>  Use Specific Channels For Specific Purposes For Eg.\n\n<:Invite:898601220502081556>  <#892300528892116992>   To Get Yourself Roles.\n\n<:Invite:898601220502081556>  <#887681083905286144>And Many More   For Game Related Stuff.\n\n<:Invite:898601220502081556>  <#887704388716597319>  For Music Bot Commands Guide.\n\n<:Invite:898601220502081556>   <#900273965195485194>  To Ask Any Kind Of Help Regarding Dude Hunter Discord Server And Dude Hunter YouTube Channel.\n\n<:Invite:898601220502081556>  <#900273949395542016>  For Suggestions Regarding Server Improvement.\n\n<:Invite:898601220502081556>   <#900273994895360011>  For Complaints Against Members Or Staff. (You've To Provide Possible Evidences In Forms Of Screenshots/Audio Recordings And Tag Accused Person/s For Us To Take Actions Effectively)\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def rulez5(self, ctx):
        embed = discord.Embed(
        title = "**TEXT CHANNEL RULES - PAGE 5**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  Usernames/Server Nicknames With Excessive Fonts, Emojis, Special Characters Aren't Allowed, Administration/Management/Moderation Teams Reserves All Rights To Change Such Usernames Without Any Prior Acknowledgements (Your Account Usernames Will Be As They Are, Just Will Be Set In Simple English Typography).\n\n<:dhrules:911452181553610802>  You're Supposed To Use English (Globally) And Hindi (Regionally) For Communication Within Server's Text And Voice Channels. Using Other Regional Languages Frequently/Intentionally Isn't Allowed And Eventually Will Lead To Moderation Actions Accordingly.\n\n<:dhrules:911452181553610802>  Abusing, Bullying, Scamming, Self Promoting, False Giveaways Promotions Are Strictly Prohibited In The Server, Also Regarding Above Mentioned Activities In DMs (Direct Messages) Of Server Member's We Request All Server Members To Keep Their DMs Of Using Guide Provided In <#900273994895360011> , Also You Can Block Such Person. We Usually Don't Take Actions In The Server For DMs Things Except Administration Finds Them Actionable. (Administration/Management Team Reserves All Rights To Take Necessary Actions)\n\n<:dhrules:911452181553610802>  Any Misbehaviour Against Female Members Of The Server Including Unnecessary Bothering, Enforcing, Flirting, Simping Is Zero Tolerance Offence, Administration/Management/Moderation Teams Will Take Appropriate Actions Accordingly.\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ **",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def sg(self, ctx):
        embed = discord.Embed(
        title = "**SCREENSHARING GUIDELINES**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  You Are Not Allowed To Screenshare/Stream Any Copyrighted Content If You Don't Have License Or Explicit Permission.\n\n<:dhrules:911452181553610802>  Do Not Screenshare/Stream Any Explicit/Pornographic/Child Abusing/Animal Abusing/NSFW Content. If Anyone Found, The User Will Be Directly Report Banned Without Any Prior Warning.\n\n<:dhrules:911452181553610802>  Direct/Indirect Promotion Of YouTube Or Any Social Platform Isn't Allowed Through Screensharing.\n\n<:dhrules:911452181553610802>  Screensharing Feature Is Currently Restricted To Specific Voice Channel And Allowed To Specific Roles. You'll Have To Ask Or Take Permission From Administration/Management/Moderation Teams If You Wants To Screenshare Or Stream. (In Case Of Emergency Or Lackness Of Permissions)\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def vcr(self, ctx):
        embed = discord.Embed(
        title = "**VOICE CHANNEL RULES**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  Don't Make NSFW Noises, Ear Rape Or Disturb Others In Anyway In Voice Channels Instant Server Voice Mute Will Be Given In Such Scenarios.\n\n<:dhrules:911452181553610802>  Any Kind Of Bullying/Abusive Language/Abusing Someone In Voice Channels Won't Be Tolerated.\n\n<:dhrules:911452181553610802>  After Listening Songs You're Supposed To Disconnect Music Bots From Voice Channel (When You're Only Remained Person Listening Songs And You're Leaving Music Voice Channel), Leaving Music Bots Alone In The Voice Channel After Listening Songs Frequently Will Lead You To Be Banned From Connecting Music Voice Channels.\n\n<:dhrules:911452181553610802>  Don't Use Voice Changers/Voice Recorders Or Any Kind Text-To-Speech Softwarers In Voice Channels.\n\n<:dhrules:911452181553610802>  Don't Use Words Or Phrases That Will Lead To Start Any Kind Of Controversy In Voice Channels. Racial Slurs Will Not Be Entertained.\n\n<:dhrules:911452181553610802>  Kindly Make Sure To Notify Everyone Else In Voice Channel If You're Intended To Record The Voice Conversation Through Screen Recording Or Any Other Source And Wait For Everyone's Approval Before You Do So Otherwise Administrative Actions Will Be Carried Out.\n\n<:dhrules:911452181553610802>  Don't Argue With Administration/Management/Moderation Teams About The Rules Or Any Unnecessary Stuff In Voice Channels.\n\n<:dhrules:911452181553610802>  We Aren't Actively Moderating Voice Channels So Kindly Use The Built-In Self Mute Functionality For Users That Are Disturbing However If You Believe That Someone Is Annoying Or Violating Rules Continuesly Tag Any Of The Active Administration/Management/Moderation Teams Or DM Them With Possible Evidences And Complaint About Them In <#900273994895360011> \n\n<:dhrules:911452181553610802>  Continuous Violations Of Above Mentioned Rules May Lead To Administration Actions Like Warn/Mute/Kick/Softban And Eventually Permanent Server Ban Regardless Of Any Roles Or Reputation In The Server.\n\n<:dhrules:911452181553610802> Do Not Visa Versa Of Voice Channels.\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def sr(self, ctx):
        embed = discord.Embed(
        title = "**SITUATIONAL RIGHTS**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n<:dhrules:911452181553610802>  There May Be Situations Not Covered By The Rules Or Times Where The Above Mentioned Rule May Not Fit The Situation. In Such Scenarios Administration/Management/Moderation Teams Are Trusted/Allowed/Reserves Rights To Handle The Situation Appropriately.\n\n<:Invite:898601220502081556>  Administration/Management/Moderation Teams Reserve The To Change Nicknames.\n\n<:Invite:898601220502081556>   Administration/Management/Moderation Teams Reserve The Right To Use Their Own Discretion Regardless Of Any Rule. (While Taking Moderation Actions Like Warn/Mute/Kick/Softban/Ban In Above Mentioned Situations)\n\n<:Invite:898601220502081556>  Administration/Management/Moderation Reserve The Right To Delete Any Post In Forms Of Images/Audios/Videos.\n\n<:Invite:898601220502081556>  Administration/Management/Moderation Reserve The Right To Disconnect, Mute, Deafen, Or Move Members To And From Voice Channels.\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green()
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)



    @commands.command()
    async def r(self, ctx):
        embed = discord.Embed(
        title = "**TRUST & SAFETY**",
        description = "**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n🔥  You Can Report Users For\n\n<:Invite:898601220502081556>   Unsolicited messages and advertisements.\n\n<:Invite:898601220502081556>   Mass server invite.\n\n<:Invite:898601220502081556>   Multiple messages with the same content over a short period of time.\n\n<:Invite:898601220502081556>   Advertising for others to join your server with the promise to join their server in return.\n\n<:Invite:898601220502081556>   Verbal abuse, harassment, spamming, raiding, scams, frauds.\n\n<:Invite:898601220502081556>   Selling Hacks, UC, Diamonds, Ingame coin's.\n\n🔥 Just Submit A Request Under Trust & Safety, Select Report Type And Provide Message Link.\n\n🔥 Use The Link Below :-\nhttps://dis.gd/request\n\n**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**",
        color = discord.Color.green(),
        )

        await ctx.message.delete()

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Rules(client))
