# 获取中国休假日

~~找了一圈GitHub，都没有发现自己需要的：需要将非工作日（包括节假日（ day_type = 0）、周末（只要是周末，不管是否调休 day_type = 2））与工作日（ day_type = 1）区分开来，写入json文件，或者拼装sql文件~~

**工作日为 1，非工作日为0，调休而变成的工作日也是 1**

通过爬取 [http://holidays-calendar.net](http://holidays-calendar.net/calendar_zh_cn/china_zh_cn.html) 网址获取公共假日

>目前只支持中国的，屏蔽调休上班日期

## 测试

```python

index.py    是执行测试文件
data.json   是自动生成的， 抓取处理后的2021年节假日json文件（结果可以自己处理，具体见参考holidays.py的67行）
openday.sql 是自动生成的，拼装的sql文件
jsonToCsv.py 是把data.json处理成csv文件



##特殊处理

   ['2月7日（星期日）、2月20日（星期六）'] 
   ['4月25日（星期日）、5月8日（星期六）']
   ['9月18日（星期六）']
   ['9月26日（星期日）、10月9日（星期六）']
   
   本代码里原本调休的工作，也作为正常周末处理，通过抓取“调休上班】(.+)上班”进行处理

```

## 结果

{"202101": {"20210101": 0, "20210102": 0, "20210103": 0, "20210104": 1, "20210105": 1, "20210106": 1, "20210107": 1, "20210108": 1, "20210109": 2, "20210110": 2, "20210111": 1, "20210112": 1, "20210113": 1, "20210114": 1, "20210115": 1, "20210116": 2, "20210117": 2, "20210118": 1, "20210119": 1, "20210120": 1, "20210121": 1, "20210122": 1, "20210123": 2, "20210124": 2, "20210125": 1, "20210126": 1, "20210127": 1, "20210128": 1, "20210129": 1, "20210130": 2, "20210131": 2}, "202102": {"20210201": 1, "20210202": 1, "20210203": 1, "20210204": 1, "20210205": 1, "20210206": 2, "20210207": 1, "20210208": 1, "20210209": 1, "20210210": 1, "20210211": 0, "20210212": 0, "20210213": 0, "20210214": 0, "20210215": 0, "20210216": 0, "20210217": 0, "20210218": 1, "20210219": 1, "20210220": 1, "20210221": 2, "20210222": 1, "20210223": 1, "20210224": 1, "20210225": 1, "20210226": 1, "20210227": 2, "20210228": 2}, "202103": {"20210301": 1, "20210302": 1, "20210303": 1, "20210304": 1, "20210305": 1, "20210306": 2, "20210307": 2, "20210308": 1, "20210309": 1, "20210310": 1, "20210311": 1, "20210312": 1, "20210313": 2, "20210314": 2, "20210315": 1, "20210316": 1, "20210317": 1, "20210318": 1, "20210319": 1, "20210320": 2, "20210321": 2, "20210322": 1, "20210323": 1, "20210324": 1, "20210325": 1, "20210326": 1, "20210327": 2, "20210328": 2, "20210329": 1, "20210330": 1, "20210331": 1}, "202104": {"20210401": 1, "20210402": 1, "20210403": 0, "20210404": 0, "20210405": 0, "20210406": 1, "20210407": 1, "20210408": 1, "20210409": 1, "20210410": 2, "20210411": 2, "20210412": 1, "20210413": 1, "20210414": 1, "20210415": 1, "20210416": 1, "20210417": 2, "20210418": 2, "20210419": 1, "20210420": 1, "20210421": 1, "20210422": 1, "20210423": 1, "20210424": 2, "20210425": 1, "20210426": 1, "20210427": 1, "20210428": 1, "20210429": 1, "20210430": 1}, "202105": {"20210501": 0, "20210502": 0, "20210503": 0, "20210504": 0, "20210505": 0, "20210506": 1, "20210507": 1, "20210508": 1, "20210509": 2, "20210510": 1, "20210511": 1, "20210512": 1, "20210513": 1, "20210514": 1, "20210515": 2, "20210516": 2, "20210517": 1, "20210518": 1, "20210519": 1, "20210520": 1, "20210521": 1, "20210522": 2, "20210523": 2, "20210524": 1, "20210525": 1, "20210526": 1, "20210527": 1, "20210528": 1, "20210529": 2, "20210530": 2, "20210531": 1}, "202106": {"20210601": 1, "20210602": 1, "20210603": 1, "20210604": 1, "20210605": 2, "20210606": 2, "20210607": 1, "20210608": 1, "20210609": 1, "20210610": 1, "20210611": 1, "20210612": 0, "20210613": 0, "20210614": 0, "20210615": 1, "20210616": 1, "20210617": 1, "20210618": 1, "20210619": 2, "20210620": 2, "20210621": 1, "20210622": 1, "20210623": 1, "20210624": 1, "20210625": 1, "20210626": 2, "20210627": 2, "20210628": 1, "20210629": 1, "20210630": 1}, "202107": {"20210701": 1, "20210702": 1, "20210703": 2, "20210704": 2, "20210705": 1, "20210706": 1, "20210707": 1, "20210708": 1, "20210709": 1, "20210710": 2, "20210711": 2, "20210712": 1, "20210713": 1, "20210714": 1, "20210715": 1, "20210716": 1, "20210717": 2, "20210718": 2, "20210719": 1, "20210720": 1, "20210721": 1, "20210722": 1, "20210723": 1, "20210724": 2, "20210725": 2, "20210726": 1, "20210727": 1, "20210728": 1, "20210729": 1, "20210730": 1, "20210731": 2}, "202108": {"20210801": 2, "20210802": 1, "20210803": 1, "20210804": 1, "20210805": 1, "20210806": 1, "20210807": 2, "20210808": 2, "20210809": 1, "20210810": 1, "20210811": 1, "20210812": 1, "20210813": 1, "20210814": 2, "20210815": 2, "20210816": 1, "20210817": 1, "20210818": 1, "20210819": 1, "20210820": 1, "20210821": 2, "20210822": 2, "20210823": 1, "20210824": 1, "20210825": 1, "20210826": 1, "20210827": 1, "20210828": 2, "20210829": 2, "20210830": 1, "20210831": 1}, "202109": {"20210901": 1, "20210902": 1, "20210903": 1, "20210904": 2, "20210905": 2, "20210906": 1, "20210907": 1, "20210908": 1, "20210909": 1, "20210910": 1, "20210911": 2, "20210912": 2, "20210913": 1, "20210914": 1, "20210915": 1, "20210916": 1, "20210917": 1, "20210918": 1, "20210919": 0, "20210920": 0, "20210921": 0, "20210922": 1, "20210923": 1, "20210924": 1, "20210925": 2, "20210926": 1, "20210927": 1, "20210928": 1, "20210929": 1, "20210930": 1}, "202110": {"20211001": 0, "20211002": 0, "20211003": 0, "20211004": 0, "20211005": 0, "20211006": 0, "20211007": 0, "20211008": 1, "20211009": 1, "20211010": 2, "20211011": 1, "20211012": 1, "20211013": 1, "20211014": 1, "20211015": 1, "20211016": 2, "20211017": 2, "20211018": 1, "20211019": 1, "20211020": 1, "20211021": 1, "20211022": 1, "20211023": 2, "20211024": 2, "20211025": 1, "20211026": 1, "20211027": 1, "20211028": 1, "20211029": 1, "20211030": 2, "20211031": 2}, "202111": {"20211101": 1, "20211102": 1, "20211103": 1, "20211104": 1, "20211105": 1, "20211106": 2, "20211107": 2, "20211108": 1, "20211109": 1, "20211110": 1, "20211111": 1, "20211112": 1, "20211113": 2, "20211114": 2, "20211115": 1, "20211116": 1, "20211117": 1, "20211118": 1, "20211119": 1, "20211120": 2, "20211121": 2, "20211122": 1, "20211123": 1, "20211124": 1, "20211125": 1, "20211126": 1, "20211127": 2, "20211128": 2, "20211129": 1, "20211130": 1}, "202112": {"20211201": 1, "20211202": 1, "20211203": 1, "20211204": 2, "20211205": 2, "20211206": 1, "20211207": 1, "20211208": 1, "20211209": 1, "20211210": 1, "20211211": 2, "20211212": 2, "20211213": 1, "20211214": 1, "20211215": 1, "20211216": 1, "20211217": 1, "20211218": 2, "20211219": 2, "20211220": 1, "20211221": 1, "20211222": 1, "20211223": 1, "20211224": 1, "20211225": 2, "20211226": 2, "20211227": 1, "20211228": 1, "20211229": 1, "20211230": 1, "20211231": 1}}

```log



