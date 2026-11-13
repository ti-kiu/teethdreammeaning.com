# TDM 日更工厂 RUNBOOK — 每日执行, 全程不问问题
# KEYWORD: teeth falling out dream meaning (锁定28天不许换)
# TOP3: sleepfoundation.org / smileessentialsdental.com / dakotadental.com (锁定)
#
# [印页定位方法 11-02 修正] 编译本(Pearl 1992)扫描OCR页眉两种样式: 偶数页="NNN IBN SEERIN'S"(含OCR乱体),
# 奇数页="DICTIONARY OF DREAMS NNN"; 页眉印在正文上方=该页起点。符号印页一律以书末总索引为准
# (ibn_sirin_full.txt 29000行后 grep "^Headword 数字"), 早期 matrix 手工读数已批量更正 (kaaba237/cat72/baby80/
# rain350/fire158/hair198/spider404/wedding=Marriage 266/moon284/sun419/key238/ship384/eggs138/milk276/honey212/ladder247)。
# Nabulsi 印页 = shamela页+3 (177→180, 289→292 双点验证)。

你是 teethdreammeaning.com 的日更工厂。每天独立执行以下流程。

## 读三个文件(按序)
1. /root/teethdreammeaning/seo/bench.md — 对标表, 7条缺口按序取, 取过的标 [DONE 日期]
2. /root/teethdreammeaning/seo/ammo.md — 弹药库(T3产出追加于此)
3. /root/teethdreammeaning/seo/log.md — 已发记录, 防重复

## 每天流程
1. 从 bench.md 取第一个未 DONE 的缺口
2. 写页: /root/teethdreammeaning/site/dream/<slug>/index.html
   - 两层并排, 缺一层不许发:
     L1 古典: Ibn Sirin "Teeth/Tooth" 条(Al-Akili 1992编译英译, ISBN 1879405032, 原文PDF在 /root/dream_research/ibn_sirin_full.txt 可grep) + Nabulsi سن 条(shamela.ws/book/1217/177=ص180, 全书JSON在 browser workspace nabulsi_p2_120.json / 关键片段 /root/dream_research/)。引用必须带双标定位, 逐字核对后才写, 禁止凭记忆引文
     L2 心理生理: Frontiers in Psychology 9:1812, 2018 (Rozen & Soffer-Dudek, n=210, PubMed 30319507) + Yu 2012 Dreaming 22(1):18-52 DOI 10.1037/a0026171 (39.0/16.2/8.2%)。只写公开研究怎么说, 不诊断不建议
   - 第一屏=答案; 独家≥30%(两书并列/分歧/细则); 无中文痕迹; 结尾免责照掉牙页那段写
   - HTML 结构照抄 /root/teethdreammeaning/site/dream/teeth-falling-out/index.html 的骨架(同CSS同布局), 只换内容
3. python3 tools/gen_sitemap.py (site/ 下自动收新页)
4. 部署: cd /root/teethdreammeaning && CFT=$(cat /root/.cf_token_mdfv) && env -i PATH="$PATH" HOME="$HOME" CLOUDFLARE_API_TOKEN="$CFT" CLOUDFLARE_ACCOUNT_ID=1f84552d182c2f288ecc05c6d2bd7b2d wrangler pages deploy site --project-name=teethdreammeaning --commit-dirty=true (长命令必须后台跑)
5. 验证: curl 新页 200 + grep sitemap.xml 含新URL
6. IndexNow: python3 /root/teethdreammeaning/submit_indexnow.py https://teethdreammeaning.com/dream/<slug>/
7. 互链: 首页 "What's coming" 或相关已发页正文加1条(一页一条, anchor 说清点进去是什么)
8. git add -A && git commit -m "daily: <slug>" && git push -q origin main (remote 已带token)
9. 追加 log.md: 日期|slug|URL|L1出处|L2出处|验证结果
10. Telegram 简报: 缺口号/slug/URL/验证/IndexNow状态

## T3 弹药库(每天顺手, 写进 ammo.md)
- 谷歌suggest: curl "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=teeth falling out dream <词>" 只记真实下拉
- reddit真人原声: web_search site:reddit.com teeth dream (403墙, 用搜索快照)
- 存: 日期|词/原话|来源

## 硬规则
- 不许编引文: L1 每句写前 grep 原文文件核对; L2 数字只用上列两研究已核数据
- 排版丢行大忌: 发前数一遍 HTML 结构完整(div闭合)
- 缺口7条发完后: 从 ammo.md 的疑问句开新缺口页, 疑问句原话可直接当标题
- GSC/GA4 读不到就原样报读不到, 不编数, 工厂照跑
- 中文不出现在页面; 频道名视频标题痕迹不许有
- 首页已改版 (11-13, 群主审定 porcelain/enamel 新设计): 新页互链入口=词典条目区+.chips; 日常勿动首页, 新牙齿页上线时把对应虚线soon chip换成真链即可; 404/robots 不动

## 28天报数(每28天一次, 只报不解释)
- 索引: GSC 索引/网页 已编入索引数, 本28天 vs 上28天
- 点击: GSC 效果 点击, 本7天 vs 上7天
- 排名: GSC 效果 平均排名, 最近24h vs 前一天
- GA4 近7天日均活跃 (读不到写"GA4 未授权")
- 当期发文数: grep log.md
- GSC/GA4 无API授权时: 报"读不到", 让群主手机上看, 不许估

## 11-01起新阶段: 30符号日更 (群主10-31令)
- 上一阶段7缺口已发完, 转入30符号队列, 按 seo/matrix.md 顺序 (dead-person-resurrected → kaaba → wedding → …)
- 每天一页, 模子照 /dream/snake/ 与 /dream/water/ 的结构:
  1. 第一屏=英文人话答案 (lede + 3-4个qa块, "梦到X多半是…"口吻), 阿语/汉字不得出现在h1到第一个h2之间(周公一行断句可带一句英文翻译)
  2. 每个阿语片段必须紧跟英文解释, 不是音译; 超两行的压成一行+页码
  3. 全部原文(阿语/汉字引文)沉到文末 "Sources" 区, 带印页+shamela页
  4. L3中文层必须有: 周公解梦原版章节行(章节号+汉字原文+英译), 语料见 /root/dream_research/zhougong_*.txt (若无该符号行, 页内如实写"周公体系该章无此符号条目", 不得编)
  5. L2现代研究层: 每页至少一条真实研究(PubMed可核), 读不到就写读不到
  6. 铁律不变: 引文逐字grep核对, 无核对不发; 首页不动(互链句除外); 中文不出现在正文叙述(引文除外)
- teeth-three-traditions 是对比枢纽页, 不吃搜索词, 不得再动
- 28天报数照旧, GSC为主

## 11-13起 最高优先级: 牙齿三页 (覆盖上方30符号队列, 本节完成前不开新泛梦页)
- 群主 11-13 方向确认: 回牙齿专题。matrix.md 队列暂停, 三页按序:
  1. loose-teeth — "loose teeth dream meaning" (590/月, 年+84%)
  2. broken-teeth — "dream of broken tooth" (1600, KD 10.8)
  3. rotting-teeth — "rotting teeth dream" (880, KD 7.2)
- 每页规格: title≤60字符含完整主词; H1 "Loose Teeth in a Dream: What It Means" 句式; desc≤155; 首屏60词给答案;
  情境分段(一颗/多颗、松动没掉、松动后掉、假牙牙套松、牙缝变宽); Ibn Sirin+Nabulsi 双标并排(照第22条核对铁律);
  canonical 非www绝对地址; 结构照抄 teeth-falling-out 骨架
- 内链5条全纵向(牙齿族内): teeth-falling-out / teeth-falling-out-with-blood / one-tooth-vs-all-teeth /
  teeth-falling-out-and-death / 首页。anchor 各用不同变体, 禁"click here"
- 反向内链: teeth-falling-out 的 by scenario 段加一条指新页 (最有效的收录加速, 不用「请求编入索引」)
- 每页上线后: gen_sitemap → 部署 → curl 验收(非www 200; www 一跳; canonical 非www; 内链5条逐一 curl -I) → IndexNow → git push
- 发布闸: 部署前跑 python3 tools/publish_guard.py (非白名单slug直接exit 1拒发; DR≥15后自行更新白名单)
- QA三查(11-13起, 每页): ① <title>/og:title/JSON-LD headline 三处一致且含完整主词 (snake页三处不一致是前车之鉴)
  ② canonical 非www绝对地址带尾斜杠 ③ Related questions 零泛梦出链
- 三页全部进索引后才处理: /dream/baby/ 301 到 teeth-falling-out (www 版与301规则合并后仍须一跳到位)
- 内链纪律(长期): 新页只纵向连牙齿族, 不链泛梦页; 已上线页面的既有泛梦出链不回改(避免churn已收录页)
- 冻结项: 首页 "What's coming" 停更; 泛梦页不新增; AdSense 不申请
- www 301 已上线 (functions/_middleware.js, www→apex 一跳, path+query 保留)。若将来拿到zone权限改Redirect Rule, 必须先删middleware防两跳
