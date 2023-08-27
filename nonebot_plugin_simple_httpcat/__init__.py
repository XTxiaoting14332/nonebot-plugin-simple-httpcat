from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, escape
from nonebot.plugin import PluginMetadata

help_text = f"""
/cat [http_status_code]
""".strip()

__plugin_meta__ = PluginMetadata(
    name = 'httpcat-状态猫😺',
    description = '简单粗暴的httpcat插件，参考了zjkwdy大佬的weather_lite插件',
    usage = help_text,
    supported_adapters={"~onebot.v11"},
    homepage="https://github.com/XTxiaoting14332/nonebot-plugin-simple-httpcat",
    type="application",
)


httpcat = on_command('cat', aliases={})

@httpcat.handle()
async def _handle(matcher: Matcher, code: Message = CommandArg()):
    if code.extract_plain_text() and code.extract_plain_text()[0]!='_':
        matcher.set_arg('code', code)


@httpcat.got('code', prompt='请输入状态码！')
async def _(code: str = ArgPlainText('code')):
    if code[0]!='_':
        await httpcat.send(MessageSegment.image(file=f'https://http.cat/{escape(code)}', cache=False), at_sender=False)
    else:
        await httpcat.reject_arg('code',prompt='不要使用“_”作为前缀啊啊啊啊')