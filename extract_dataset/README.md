# VVC MTS Dataset Label Extraction Guide

본 문서는 VVC 표준 기반 MTS (Multiple Transform Selection) 레이블 추출 방법을 설명합니다.

## 1. Trace 파일 생성

1. VTM 인코더 및 디코더를 **빌드 및 릴리즈** 시 `trace 기능(trace enable)`을 활성화합니다.
2. 인코딩 및 디코딩을 수행하면, 각 과정에서 **Trace 파일**이 생성됩니다.
3. Trace 파일에는 각 CU (Coding Unit)에 대해 **MTS Type** 정보가 기록되어 있습니다.

## 2. 데이터셋 레이블 추출 절차

생성된 Trace 파일로부터 MTS 레이블을 추출하기 위해 다음 단계를 수행합니다.

### Step 1: Trace 파일 정제

- **`step1_vtmtrace_to_txt.py`** 실행
- 목적: VTM Trace 파일을 읽어 필요한 정보만 남기고 정제된 텍스트 파일로 변환합니다.

### Step 2: MTS 관련 데이터 추출

- **`step2_ex_MTS_Y.py`** 실행
- 목적: Y(루마) 성분을 기준으로 MTS Type을 추출하고 가공합니다.

### Step 3: 최종 CSV 생성

- **`step3_MTS_to_csv.py`** 실행
- 목적: 정제된 데이터를 CSV 파일로 저장하여, 이후 학습/분석에 사용할 수 있도록 준비합니다.

## 3. 최종 결과

- 최종적으로 **각 블록별 MTS index**를 포함하는 **CSV 데이터셋**이 생성됩니다.
- 해당 CSV 파일은 추후 신경망 학습 등에 레이블 데이터로 활용할 수 있습니다.

---

> ⚡ 참고: Trace 파일에서 정확한 MTS Type을 추출하려면 인코딩 설정, 인트라 모드 등 세부 옵션을 올바르게 설정하는 것이 중요합니다.
