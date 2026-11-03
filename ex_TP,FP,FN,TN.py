# ========================================
# 이진 분류 성능평가 프로그램
# TP = True Positive
# FP = False Positive
# FN = False Negative
# TN = True Negative
# ========================================

# 혼동행렬 값 사용자 입력
TP = int(input("TP(True Positive) 입력: "))
FP = int(input("FP(False Positive) 입력: "))
FN = int(input("FN(False Negative) 입력: "))
TN = int(input("TN(True Negative) 입력: "))

# 입력값 검증
if min(TP, FP, FN, TN) < 0:
    print("오류: 음수는 입력할 수 없습니다.")

else:
    # 전체 데이터 수
    N = TP + FP + FN + TN

    if N == 0:
        print("오류: 전체 데이터 수가 0입니다.")

    else:
        # 1. 정확도 Accuracy
        accuracy = (TP + TN) / N

        # 2. 민감도 Sensitivity / Recall
        sensitivity = TP / (TP + FN) if TP + FN != 0 else 0

        # 3. 특이도 Specificity
        specificity = TN / (TN + FP) if TN + FP != 0 else 0

        # 4. 정밀도 Precision / PPV
        precision = TP / (TP + FP) if TP + FP != 0 else 0

        # 5. 음성예측도 NPV
        npv = TN / (TN + FN) if TN + FN != 0 else 0

        # 6. F1-score
        f1_score = (
            2 * precision * sensitivity / (precision + sensitivity)
            if precision + sensitivity != 0 else 0
        )

        # 7. 오류율 Error Rate
        error_rate = (FP + FN) / N

        # 혼동행렬 출력
        print("\n========== 혼동행렬 ==========")
        print("                 실제 +     실제 -")
        print(f"예측 +           {TP:5d}      {FP:5d}")
        print(f"예측 -           {FN:5d}      {TN:5d}")

        # 성능 평가 출력
        print("\n========== 성능 평가 ==========")
        print(f"정확도 Accuracy       : {accuracy:.2%}")
        print(f"민감도 Sensitivity    : {sensitivity:.2%}")
        print(f"특이도 Specificity    : {specificity:.2%}")
        print(f"정밀도 Precision      : {precision:.2%}")
        print(f"음성예측도 NPV        : {npv:.2%}")
        print(f"F1-score              : {f1_score:.2%}")
        print(f"오류율 Error Rate     : {error_rate:.2%}")

        # 오류 해석
        print("\n========== 오류 해석 ==========")
        print(f"FP(False Positive) = {FP}")
        print("-> 실제 음성을 양성으로 잘못 판단")
        print("-> 불필요한 검사나 처치 등 비용 발생 가능")

        print(f"\nFN(False Negative) = {FN}")
        print("-> 실제 양성을 음성으로 잘못 판단")
        print("-> 질병이나 이상을 놓치는 위험 발생 가능")
