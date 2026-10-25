# 工作流程紀錄 (Workflow Log)

## 流程節點
- [x] 階段 1：建立需求規範 (`research/requirements.md`) 與來源證據帳本 (`research/source-ledger.md`)
- [x] 階段 2：調用 Claude Code 撰寫深度導讀核心 Markdown (`guide.md`)
- [x] 階段 3：總編審查與事實分級核對（已完成來源標籤分類與詞彙校準）
- [x] 階段 4：轉製發布就緒 HTML (`index.html`)，整合響應式排版、深淺主題切換、Mermaid 直屏圖與資料卡
- [x] 階段 5：版面與功能驗收（QA Check 全數通過：0 Error, 0 Warning）
- [x] 階段 6：交付檢核與 README

## 模型與調用宣告
- 主控統籌：Antigravity (Gemini 3.8 Flash)
- 核心撰稿與審查：Claude Code (`/Users/lanss/.local/bin/claude` / Claude Sonnet 5.5)
- 規範依循：`deep-guide-html` (v2.1)
- 產出檔案：
  - `index.html` (26 KB)
  - `guide.md` (17 KB)
  - `starlink_ukraine_analysis.md` (4.5 KB)
