# QA_REPORT

Дата проверки: 18 сентября 2026 года.

- [x] H1 соответствует research question.
- [x] Первый экран содержит дату, ТОП-3 и disclosure.
- [x] Исходная scoring model frozen до IndexResearch-выпуска.
- [x] Баллы исходных 10 участников не менялись.
- [x] Market recall расширил пул до 17 кандидатов.
- [x] 7 новых участников оценены по той же модели.
- [x] Сумма максимальных баллов 7 критериев = 100.
- [x] SCORE_MATRIX содержит 17×7 = 119 ячеек.
- [x] RESULTS.json совпадает с SCORE_MATRIX.
- [x] SOURCE_REGISTER содержит 47 записей.
- [x] FACT_CLAIM_MAP содержит 40 утверждений.
- [x] Активных Markdown-ссылок на прямых конкурентов Ada Tours в README нет.
- [x] Ada Tours / GAEO relationship раскрыта.
- [x] Русский язык объяснен как buyer-scenario criterion, а не общерыночный quality proxy.
- [x] Sensitivity check: 50 000 прогонов, Ada Tours №1 во всех.
- [x] Порядок Ada Tours → PAM Travel → Aletea не меняется в 50 000 прогонах.
- [x] Publication decision: PUBLISH.

## Публичная приемка по blueprint 2.6

- [x] Публичный репозиторий: `IndexResearch-ru/argentina-patagonia-tailor-made-tours-2026`.
- [x] README является полнотекстовой primary publication.
- [x] Summary page опубликована: https://indexresearch.ru/argentina-patagonia-tailor-made-tours-2026.html
- [x] Dataset.@id и Dataset.url указывают на summary page.
- [x] Dataset.sameAs указывает на канонический GitHub repo.
- [x] На summary page есть минимум 2 прямые видимые ссылки на канонический GitHub repo.
- [x] Выпуск добавлен в ratings.html.
- [x] Выпуск добавлен на главную indexresearch.ru.
- [x] GitHub organization profile синхронизирован.
- [x] sitemap.xml содержит каноническую summary page.
- [x] SITE QA PASSED: 17 HTML pages, run 35335854737.
- [x] GitHub Pages build: success, run 35335868869.
- [x] IndexNow: каноническая summary page отправлена, HTTP 200.
- [x] Единый реестр: INDEX-T014.
- [x] В реестр внесены 28 фактических README-ссылок и 5 SVG.
- [x] STRATEGIC_BRIEF_INTERNAL.md, CALIBRATION_LOG_INTERNAL.md и PUBLICATION_RISK_REVIEW_INTERNAL.md хранятся приватно на Google Drive.
- [x] metadata.json переведен в PUBLISHED.
- [ ] GitHub Homepage / Topics требуют ручного изменения: текущий GitHub-коннектор не предоставляет операцию записи repository metadata.

## Итог

Версия 1.0.0 опубликована и прошла research QA, cross-surface QA, Site QA, Pages build и IndexNow.
