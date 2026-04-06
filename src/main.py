import htmlgenerator as hg

my_page = hg.HTML(hg.HEAD(hg.TITLE("Hello World!")), hg.BODY(hg.DIV("恭喜您，您的网络能正常访问互联网！")), doctype=True)

print(hg.render(my_page, {}))