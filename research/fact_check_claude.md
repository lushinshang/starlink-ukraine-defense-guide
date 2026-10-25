# 烏克蘭星鏈爭端五大主張：事實查核報告

> 查核日期：2026-10-26。方法：WebSearch 加 WebFetch 讀原文，比對 Kutkov 部落格、TopWar 原文、Kyiv Independent、UNITED24、AP/ABC、DroneXL。
> **沒讀到原文的部分**：WSJ（付費牆，只能經二手轉述）、state.gov 的 Rubio 逐字稿（只讀到搜尋摘要）、Serhii Flash 的 Telegram 原貼文。

## 總覽

| 主張 | 查核結論 | 證據強度 |
|---|---|---|
| 一、160 km/h 速限 | **部分正確**：年份錯了（應為 2026，不是 2024），受影響的是 Starshield，宣布解除的主體也不精確 | 一手官方加外媒具名報導 |
| 二、烏軍焊入 GPS 破解板 | **無證據**，而且和 Kutkov 原文的性質不同 | 單方推論 |
| 三、伺服器端用天體物理檢測 | **未經證實**，三個機制在物理上的合理程度差很多 | 單方推論假說 |
| 四、歐洲地面站縱火 | **事件屬實**，但歸因和「暗網接單」的細節要拆開看 | 一手官方（波蘭、立陶宛）、外媒報導（保加利亞） |
| 五、Rubio／WSJ／ToS | **發言屬實**，但 Rubio 的說法本身有爭議，各方說法互相矛盾 | 一手官方加外媒具名調查 |

---

## 主張一：100 mph 速限、Serhii Flash 披露、10/24 解除

**【查核結論】部分正確，有三處要改**
1. **年份錯誤**：速限是 **2026 年 10 月 14 日**才出現的（Reuters 同日報導，BusinessDay／TimesLive 有轉載）。2024 年 10 月 14 日沒有這件事。專案的 `research/source-ledger.md` 把來源編成 `UKR-FLASH-2024`，日期也寫 2024，**這兩處都錯**。
2. **受影響的系統**：多數報導指受限的是 **Starshield（軍用版）**的終端，不是一般商用 Starlink。Zelensky 則說兩種服務都受影響。
3. **誰宣布解除**：10/24 是**烏克蘭國防部**先宣布 Starshield 恢復到 400 km/h 以上，Zelensky 同日確認「速度已回到該有的水準」。他前一天（10/23）還說限制仍在。另外 10/14 晚間曾先部分恢復到 160 km/h 以內。

另外要補兩點背景：
- 2026 年 1 月底有過一次**性質不同的速限**（約 75–90 km/h）。那次是烏克蘭國防部主動要求的，用來阻止**俄軍**的打擊無人機使用 Starlink，登記在白名單上的烏軍終端可以豁免。兩次不能混為一談。
- 「攔截機時速 180–300 km/h」這個數字我**查不到來源**。比較可靠的說法是：Beskrestnov 指攔截機要追的是噴射動力 Shahed（Geran-3 類），而國防部說恢復後支援 400 km/h 以上。

**【證據強度】** 一手官方（烏克蘭國防部、Zelensky、Beskrestnov 公開發言）加外媒具名報導（Reuters、Axios、Bloomberg、NPR、CNBC）。

**【技術可行性】** 很高。Starlink 本來就有依方案劃分的速度門檻，例如 Roam／Priority 方案可在約 160 km/h 以內移動使用。終端內建 GPS、IMU，相控陣天線也能測 Doppler，可以估算移動速度。

**【修正文句建議】**
> 2026 年 10 月 14 日，總統顧問 Serhii「Flash」Beskrestnov 披露 SpaceX 將烏軍 Starshield 終端的可用移動速度限制在約 160 km/h（100 mph），用來攔截噴射動力 Shahed 的高速攔截無人機因此受影響。10 月 24 日，烏克蘭國防部宣布恢復 400 km/h 以上的運作，Zelensky 同日確認。

---

## 主張二：烏軍焊入「GPS 破解板」偽造靜止座標

**【查核結論】查無可信證據，Kutkov 的工作也被錯誤引用**

我直接讀了 Kutkov 2023-11-07 的原文《Connecting external GPS antenna to the Starlink terminal》，內容和 ledger 的描述對照如下：

| ledger 的描述 | Kutkov 原文實際寫的 |
|---|---|
| STA8089 晶片 | ✅ 正確。初版終端用 STA8090，後來改用比較便宜的 STA8089（都是 ST Teseo 車規等級 GNSS 晶片） |
| 陶瓷天線被電戰燒毀，所以焊跳線 | ⚠️ 不精確。原文的問題是內建晶片天線「增益低、全向」，會同時收到干擾。後果是終端「卡在開機狀態」，最壞情況是 **STA8089 或 LNA** 被強 RF 損壞，不是天線燒毀。做法是拆掉晶片天線、把同軸線焊到 50Ω 饋點、外接主動天線（用 Bias-T 供電）、加裝防水 **SMA** 接頭 |
| 防水 RJ45 | ❌ **原文沒有提到** |
| 「速限由伺服器端配置，本地竄改騙不了核心網」 | ❌ **原文沒有提到**。只有作者在留言區說過，以 cell 為單位的服務限制「not about GPS」 |
| 偽造座標 | ❌ 原文目的是**抗干擾、讓終端收得到真實 GPS**，不是偽造。作者還警告不要拿 jammer／spoofer 近距離照射終端 |

**關鍵差異**：Kutkov 做的是「讓終端在電戰環境下**收得到真實訊號**」，主張二講的是「**偽造**座標」，兩者目的相反。

**歸屬錯位**：我找到唯一提到「用代理板（proxy board）偽造速度資料」的報導，是 DroneXL 2026-01-31 的文章。文中指的是**俄方**操作員用這種板子繞過更早期約 40 km/h 的門檻，而且只有這一個來源。目前**沒有任何可信來源**指出烏軍大規模焊入破解板。目前查得到的出處只有 Substack（simplicius76），以及 TopWar 轉述的「另一種版本」。

**單靠焊板能不能騙過核心網？** 我判斷不太可能完全騙過。終端回報的 GPS 只是其中一個訊號來源，網路端還能拿到下列物理量：
- 鏈路的 timing／ranging
- Doppler 殘差
- 波束與 cell 的對應關係

座標造假會和這些量互相矛盾。不過 SpaceX 從未公開它實際用哪些檢查，所以這個判斷**屬於推論，未驗證**。

**【證據強度】** 單方推論。Kutkov 原文是一手工程文件，但內容和這個主張無關。

**【修正文句建議】**
> 烏克蘭工程師 Oleg Kutkov 曾公開改裝方法：把 Starlink 終端內建的 GNSS 晶片天線（搭配 STA8089 接收器）換成外接主動天線，讓終端在 GPS 干擾下仍能定位上線。至於「焊入破解板偽造靜止座標」的說法，目前沒有可信來源證實；公開報導中唯一的「速度偽造板」案例，指向的是 2026 年初的俄方用戶。

---

## 主張三：用 Doppler、H3 波束脫靶、Handover 頻率檢測座標造假

**【查核結論】未經證實的推論假說。連 TopWar 自己都否定了其中一部分**

TopWar 原文（Макс Вектор，2026-10-25）的立場：
- 它稱這套說法是「方便的技術傳說，尚未成為確立的事實」（«Удобная техническая легенда пока не стала установленным фактом»）。
- 它直接說「單憑換手**不能**證明載具的速度」（«Само переключение не доказывает скорость носителя»）。
- 它寫明 SpaceX 沒有公開檢測方法，「把具體演算法歸給 SpaceX 為時過早」。
- **原文完全沒有提到 Doppler 和 H3**。這兩項是後來不知哪一方加上去的，來源不明。

SpaceX 和 Musk 方面也沒有說明機制。Musk 10/24 只說「That loophole was closed last week」，而他在 10/14 的說法卻是 Starshield 的限制「由美軍與總統決定」。**他自己前後說法就互相矛盾。**

**【技術可行性】**（以下是 AI 的物理推算，未經實測）

| 機制 | 物理上是否合理 | 理由 |
|---|---|---|
| **Doppler 矛盾** | 🟢 原理上可行，三者中最強 | 衛星本身造成的 Doppler（Ku 頻段可達數百 kHz）能用星曆精確預測，扣除後剩下的殘差反映終端自身運動。用 Δf ≈ v/c × f 粗估，時速 300 km/h（約 83 m/s）在 12 GHz 約產生 3 kHz 偏移，量級上測得到 |
| **H3 cell 波束脫靶** | 🟡 可能可行 | Starlink 的服務地圖確實以 H3 六角格劃分。高速載具會在幾分鐘內跨格，排程的波束和實際位置不符時會讓鏈路品質下降。但這比較像「造成連線變差」，不一定被當成「檢測」機制 |
| **Handover 頻率超標** | 🔴 最弱 | 衛星對地速度約 27,000 km/h，時速 300 km/h 的無人機只占約 1%，對換星頻率影響很小。學界量測也指出 Starlink 本來就有約 15 秒一次的全網排程重配，不論終端動不動。這正是 TopWar 否定它的理由（15 秒這個數字是根據我對既有量測研究的記憶，這次沒有重新查證） |

**【證據強度】** 單方推論假說。沒有任何官方文件，也沒有可重現的實測。

**【修正文句建議】**
> SpaceX 沒有公開怎麼辨識超出方案的移動狀態。坊間流傳的「換手頻率檢測」說法，連最早轉述它的俄方媒體 TopWar 都認為沒有證據，而且在物理上站不住腳，因為靜止終端同樣會頻繁換星。理論上，Doppler 殘差或鏈路時序比對是比較可行的識別方式，但這只是推測。

---

## 主張四：波蘭、保加利亞、立陶宛設施遭縱火

**【查核結論】三起事件都屬實，但確鑿程度不同；「暗網接單」與金額沒有查證到**

| 事件 | 日期 | 已查證的事實 | 歸因 |
|---|---|---|---|
| 波蘭 Wola Krobowska（華沙南方約 40 km，國營電信 Exatel 營運） | 9/23 | 縱火損壞供電系統與發電機，烏軍等用戶的連線中斷，之後已恢復。10/12 宣布**兩名土耳其籍嫌犯在德國被捕** | **一手官方**：國家檢察署發言人 Nowak 說「合理懷疑受俄國特勤指使」；內政部長 Siemoniak 說「毫無疑問是俄情報機構所為」；Tusk 稱之為混合戰。不過早期報導也曾考慮短路的可能 |
| 保加利亞 Plana（索菲亞南方） | 10/9（10/12 才曝光） | 兩名蒙面男子縱火。**損壞天線數各方說法不一**：在野議員說 17 座中有 11 座，起訴書約 3 座全毀加數座受損，Kyiv Post 說 8 座。**兩名德國籍嫌犯**於 10/14 被缺席起訴，下落不明 | **保國官方沒有確認俄方涉入**。只有在野議員和國安首長說是蓄意破壞 |
| 立陶宛 Vilnius（Aukštieji Paneriai，資料中心業者 Delska 租給 SpaceX 的設施） | 10/18 約凌晨 2 點 | **縱火未遂**，員工自行撲滅，服務沒有受影響。截至 10/19 沒有人被捕。官方兩天前已經示警 | 總理 Sinkevičius 說「很可能是俄國」，危機管理中心把它和波蘭、保加利亞的案子連結 |

**「Telegram／暗網接單、懸賞 500–10,000 美元加密貨幣」**：讀過的原文（UNITED24、AP/ABC）都**沒有**把這些細節連到這三起案件。Siemoniak 說的是一個**普遍模式**：俄方從 2024 年起透過 Telegram 招募「用完即丟的特工」在波蘭犯案。金額數字我**找不到出處**。

**【證據強度】** 波蘭是一手官方（檢察署、部長），保加利亞和立陶宛是一手官方說明事件本身，但歸因只到「懷疑」。

**【修正文句建議】**
> 2026 年 9–10 月，波蘭 Wola Krobowska 地面站（9/23）和保加利亞 Plana 地面站（10/9）先後遭人縱火，立陶宛 Vilnius 的 Starlink 設施則發生縱火未遂（10/18）。波蘭官方直指俄國情報機構，嫌犯為兩名在德國被捕的土耳其籍人士；保加利亞已缺席起訴兩名德國籍人士，但沒有正式歸因俄方。俄方否認涉入。

刪掉「暗網接單」和具體懸賞金額，除非之後找到針對個案的來源。

---

## 主張五：Rubio、Starshield、WSJ 煉油廠報導、政策與 ToS 的界線

**【查核結論】發言屬實，但各方說法之間大量互相矛盾，不能當作定論引用**

已查證的部分：
- **Rubio 原話**（國務院逐字稿，經搜尋摘要轉述）：「They do not have access to it at this moment」。他也說 Starlink 是商用、Starshield 是軍用，兩者是「two different products」；烏方申請 Starshield 是為了打擊俄國境內縱深目標；還說「Nobody ordered that Starlink speed to be slowed down」，以及「we don't control … how [a private company] decide[s] their product can be used」。
- **Rubio 的說法被質疑**：Kyiv Independent 引述 Bloomberg，指烏克蘭從 2024 年起就在用 Starshield，先在試行計畫中拿到 500 台，2024 年底兩份五角大廈合約共提供約 3,000 台。
- **主張中「美方拒絕烏方以 Starshield 縱深打擊」這一段**：比較準確的說法是「烏方提出申請，但目前沒有取得使用權」。Kyiv Independent 也指出 Starshield 在打擊煉油廠的行動中「沒有扮演角色」，Beskrestnov 則說「物理上不可能用商用 Starlink 做縱深與中程打擊」。
- **WSJ 報導**（經 Plataforma Media、Kyiv Independent 轉述，**沒讀到原文**）：Musk 和 Trump 討論過烏軍打擊俄國柴油煉油廠（Trump 把美國油價上漲歸咎於此）之後，**親自下令**降速；後來 Trump 在 10/21 要求解除。
- **各方說法互相矛盾**：
  - Reuters 引兩名美方官員：命令出自白宮內部。
  - Trump、Rubio、Hegseth：否認曾經指示。
  - Musk 在 10/14：限制由美軍與總統決定。
  - Musk 在 10/24：烏軍違反 ToS、拿來做攻擊性打擊，漏洞已補上。

**【政策與 ToS 的界線分析】**
1. **商用 Starlink**：受 SpaceX 的 ToS 和方案條款約束，包括速度、地理範圍與用途限制，由公司片面執行。這是 Rubio「私人公司自己決定」說法的依據。
2. **Starshield**：根據 Musk 自己的說法和報導中的合約結構，Starshield 由美國政府擁有、控制，而且是透過五角大廈合約提供，所以使用限制應屬**政府政策**範疇，不是 ToS。
3. **矛盾點**：Musk 10/24 用「違反 ToS」來解釋限制，等於拿商用條款的邏輯去套軍用系統，而 Rubio 又否認烏方有 Starshield。兩人的說法**不可能同時成立**。目前公開資料無法判定是誰下的令。

**【證據強度】** 一手官方（國務院逐字稿、Musk 公開貼文）加外媒具名調查（WSJ、Reuters、Bloomberg），但各方說法互相衝突。

**【修正文句建議】**
> 美國國務卿 Rubio 10 月中表示烏克蘭「目前沒有 Starshield 使用權」，但 Bloomberg 等報導指出烏軍從 2024 年起就經五角大廈合約取得 Starshield 終端。WSJ 引述美方官員，指降速是 Musk 在和 Trump 討論烏軍打擊俄國煉油廠之後下令的；Reuters 則報導命令出自白宮。Trump 政府否認介入，Musk 前後說法也不一致。誰下令限速，目前仍無定論。

---

## 對專案檔案的影響（只列出，沒有動手改）

`research/source-ledger.md` 有幾處和查核結果不符，`guide.md` 與 `index.html` 可能沿用了相同內容：
- `UKR-FLASH-2024`：日期應改為 2026-10-14。
- `TECH-KUTKOV-2023` 第 2–4 點：防水 RJ45、伺服器端配置在原文都找不到；「陶瓷天線燒毀」不精確。這條也不能當作「烏軍焊板改裝」的原理依據。
- `RU-TOPWAR-2026`：沒有提到 Doppler 或 H3 的出處。
- `EU-SABOTAGE-2026`：暗網懸賞和金額沒有查證到；立陶宛案是未遂，地點是資料中心業者 Delska 的設施，不是倉儲。

要的話我可以依這份報告修正這些檔案。

## Sources
- [Axios：烏國防部宣布解除速限](https://www.axios.com/2026/10/24/musk-ukraine-starlink-starshield-speed)
- [Kyiv Independent：Starshield 恢復 400 km/h 以上](https://kyivindependent.com/starshield-operations-restored-above-400-km-h-ukraines-defense-ministry-says/)
- [Kyiv Independent 分析：Starshield 受限與 Rubio 說法](https://kyivindependent.com/analysis-ukraines-starshield-access-is-still-crippled-soldiers-civilians-are-paying-the-price/)
- [NBC：Musk 稱已補上 loophole](https://www.nbcnews.com/world/ukraine/elon-musk-spacex-closed-ukraine-starlink-loophole-limits-hit-drone-rcna605494)
- [CNBC](https://www.cnbc.com/2026/10/24/ukraine-starlink-starshield-service-restored.html)
- [NPR](https://www.npr.org/2026/10/24/nx-s1-6015482/ukraine-starlink-working-after-disruptions)
- [BusinessDay（Reuters 10/14）](https://www.businessday.co.za/world/2026-10-14-ukraine-says-spacex-limits-starlink-operations-disrupting-military/)
- [DroneXL：2026 年 1 月速限](https://dronexl.co/2026/01/31/spacex-starlink-speed-limit-russian-drones/)
- [Jamestown Foundation](https://jamestown.org/ukraine-responds-to-russias-starlink-use/)
- [Oleg Kutkov 原文](https://olegkutkov.me/2023/11/07/connecting-external-gps-antenna-to-the-starlink-terminal/)
- [TopWar 原文](https://topwar.ru/292301-starlink-na-tormozah-chto-proizoshlo-so-svjazju-ukrainskih-bpla.html)
- [Simplicius Substack](https://simplicius76.substack.com/p/ukraine-starlink-mystery-finally)
- [AP/ABC：波蘭歸咎俄國](https://abcnews.com/International/wireStory/poland-blames-starlink-sabotage-russia-137218051)
- [UNITED24：波蘭檢方說法](https://united24media.com/world/starlink-station-fire-in-poland-pointing-directly-to-russian-intelligence-orders-22879)
- [Euromaidan Press：保加利亞缺席起訴](https://euromaidanpress.com/2026/10/20/two-germans-charged-in-absentia-over-bulgarias-starlink-fire-one-of-three-recent-attacks-on-satellite-links-ukraine-relies-on-against-russia/)
- [Kyiv Post：保加利亞](https://www.kyivpost.com/post/87549)
- [LRT：立陶宛](https://www.lrt.lt/en/news-in-english/19/3086054/attempted-arson-at-lithuanian-firm-storing-starlink-equipment-pm-blames-russia)
- [Aerotime：立陶宛](https://www.aerotime.aero/articles/lithuania-starlink-arson-russian-sabotage/amp)
- [State Dept：Rubio 記者會](https://www.state.gov/releases/office-of-the-spokesman/2026/10/secretary-of-state-marco-rubio-remarks-to-the-press-18/)
- [Ukrinform：Rubio 稱烏方無 Starshield](https://www.ukrinform.net/rubric-polytics/4175635-rubio-says-ukraine-does-not-have-access-to-starshield.html)
- [Al Jazeera：Rubio 稱由 Musk 決定](https://www.aljazeera.com/news/2026/10/22/ukraines-access-to-starlink-a-decision-for-elon-musk-rubio-says)
- [Plataforma Media（轉述 WSJ）](https://www.plataformamedia.com/en/2026/10/21/wsj-reports-musk-himself-ordered-the-starshield-cap-that-hit-ukraines-drones-trump-rubio-and-hegseth-deny-directing-it-with-video/)
