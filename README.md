# Solana Early Radar — research showcase

Исследовательский Python/on-chain проект по проверке гипотез раннего
обнаружения интересных новых Solana / Pump.fun токенов по данным Helius API.

Это **research showcase**, а не trading bot. Realtime scoring и торговое
исполнение не запускались.

## Главный результат

Изначально повторяющиеся early-buying wallets/cohorts выглядели перспективно
на отдельных кейсах и небольшом пилоте. После более крупной temporal-проверки
гипотеза не подтвердилась как устойчивый дополнительный predictive signal.

### 500-mint milestone

- **500** независимых Pump mints;
- **2,500** frozen token-cutoff rows;
- **8,155** уникальных покупателей до T+5m;
- **838** покупателей с recurring history;
- **2,033** descriptive recurring pairs;
- **33** connected cohorts;
- Tier B base rate: **5%**.

### Validation

| Cutoff | Baseline PR-AUC | + Cohort features | Delta |
|---|---:|---:|---:|
| T+3m | 0.134 | 0.137 | +0.003 |
| T+15m | 0.162 | 0.142 | -0.020 |

Walk-forward:

- improvement in **6/20** folds;
- median delta: **-0.045**.

**Decision:** cohort features alone were not strong enough to justify a
realtime radar or trading-execution layer.

## Почему это полезный результат

Цель исследования была не получить красивый график любой ценой, а проверить
гипотезу без look-ahead leakage. После слабого out-of-sample результата
реализация realtime-системы была остановлена.

Для портфолио это показывает:

- работу с on-chain/API data;
- формирование и проверку гипотез;
- temporal feature design;
- осторожность с data leakage;
- PR-AUC и walk-forward validation;
- способность отказаться от идеи, когда данные её не подтверждают.

## Case study

До массовой проверки был сделан подробный historical case study одного токена:

- 20,876 successful transactions through T+24h;
- 1,166 meaningful first-60m buyers;
- temporal snapshots from T+1m onward;
- wallet/funder relationships;
- burstiness and concentration diagnostics;
- explicit leakage guards and limitations.

Сокращённая публичная версия находится в `ansem_case_study.md`.

## Files

```text
README.md
methodology.md
ansem_case_study.md
results.json
verify_summary.py
.env.example
.gitignore
```

`verify_summary.py` — только небольшой публичный helper, который проверяет
арифметику итоговых метрик из `results.json`. Это не production research
pipeline.

## Run

```bash
python verify_summary.py
```

## Private / omitted

Из публичной версии исключены:

- Helius API key;
- локальный cache;
- raw/backfill datasets;
- тяжёлые промежуточные artifacts;
- внутренний исследовательский pipeline.

`.env.example` содержит только placeholder.
