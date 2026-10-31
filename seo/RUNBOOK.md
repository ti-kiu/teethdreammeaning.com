# TDM 日更工厂 RUNBOOK — 每日执行, 全程不问问题
# KEYWORD: teeth falling out dream meaning (锁定28天不许换)
# TOP3: sleepfoundation.org / smileessentialsdental.com / dakotadental.com (锁定)

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
- 首页一个字节不动(除了互链那句); 404/robots 不动

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
