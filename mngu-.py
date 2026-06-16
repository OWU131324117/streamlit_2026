import streamlit as st
import random

st.markdown(
    "<h1 style='color:#7CB342;'>マンダロリアン・アンド・グローグー おすすめキャラ診断 <(｡◕‿◕｡)></h1>",
    unsafe_allow_html=True
)

st.markdown("---")
st.write("好きな属性を複数選択してください！")

cute = st.checkbox("かわいい😊")
cool = st.checkbox("かっこいい😎")
bigbro = st.checkbox("兄貴肌💪")
strong = st.checkbox("強い⚔️")
reliable = st.checkbox("頼りになる🤝")
caring = st.checkbox("面倒見がいい🤗")
unique = st.checkbox("個性的✨")
funny = st.checkbox("お茶目😆")

if st.button("診断する"):

    scores = {
        "マンドー": 0,
        "グローグー": 0,
        "ロッタ": 0,
        "ゼブ": 0,
        "エンボ": 0,
        "大佐": 0
    }

    reasons = []

    if cute:
        scores["マンドー"] += 1
        scores["グローグー"] += 2
        reasons.append("かわいい")

    if cool:
        scores["マンドー"] += 2
        scores["ロッタ"] += 1
        scores["エンボ"] += 2
        scores["大佐"] += 1
        reasons.append("かっこいい")

    if bigbro:
        scores["ゼブ"] += 2
        scores["ロッタ"] += 1
        reasons.append("兄貴肌")

    if strong:
        scores["マンドー"] += 2
        scores["ロッタ"] += 2
        scores["エンボ"] += 2
        reasons.append("強い")

    if reliable:
        scores["ゼブ"] += 2
        scores["大佐"] += 2
        scores["グローグー"] += 1
        reasons.append("頼りになる")

    if caring:
        scores["ゼブ"] += 2
        scores["大佐"] += 1
        scores["マンドー"] += 2
        reasons.append("面倒見がいい")

    if unique:
        scores["エンボ"] += 3
        reasons.append("個性的")

    if funny:
        scores["グローグー"] += 2
        reasons.append("お茶目")

    max_score = max(scores.values())

    if max_score == 0:
        st.warning("項目を1つ以上選択してください！")

    else:

        best_matches = [
            char for char, score in scores.items()
            if score == max_score
        ]

        descriptions = {
            "マンドー": """
マンドーは、強くて頼れる賞金稼ぎ。
クールな見た目とは裏腹に面倒見が良く、
大切な存在のためなら危険も恐れない人物です。
""",
            "グローグー": """
グローグーは、かわいくてお茶目な銀河の人気者。
思わず守りたくなる愛らしさと、
いざという時の頼もしさを兼ね備えています。
""",
            "ロッタ": """
ロッタは、強さと存在感が魅力のキャラクター。
堂々とした振る舞いとタフさが光ります。
""",
            "ゼブ": """
ゼブは、頼れる兄貴肌タイプ。
仲間思いで面倒見が良く、
一緒にいると安心感を与えてくれる存在です。
""",
            "エンボ": """
エンボは、個性的でクールな賞金稼ぎ。
独特なスタイルと圧倒的な存在感が魅力です。
""",
            "大佐": """
大佐は、冷静で頼りになるリーダータイプ。
状況を見極めながら仲間を支える、
落ち着いた大人の魅力があります。
"""
        }

        st.header("🎉診断結果🎉")

        if len(best_matches) == 1:
            selected_character = best_matches[0]

            st.success(
                f"あなたにおすすめのキャラクターは **{selected_character}** です！"
            )

        else:
            selected_character = random.choice(best_matches)

            st.success(
                f"あなたにおすすめのキャラクターは "
                f"**{'・'.join(best_matches)}** です！"
            )

            st.info(
                f"同点だったので、今回は **{selected_character}** の紹介を表示します！"
            )

        

        st.write(descriptions[selected_character])

        st.info(
            f"あなたは『{'・'.join(reasons)}』を重視するタイプです！"
        )

        st.subheader("🏆おすすめランキング")

        ranking = sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        total_score = sum(scores.values())

        medals = ["🥇", "🥈", "🥉"]

        for i, (char, score) in enumerate(ranking):

            percent = (
                score / total_score * 100
                if total_score > 0
                else 0
            )

            if i < 3:
                st.write(f"{medals[i]} {i+1}位：{char}")
            else:
                st.write(f"{i+1}位：{char}")

            st.progress(percent / 100)

            st.write(
                f"スコア：{score}点（{percent:.1f}%）"
            )

        with st.expander("📊詳細なスコアを見る"):

            for char, score in ranking:

                percent = (
                    score / total_score * 100
                    if total_score > 0
                    else 0
                )

                st.write(
                    f"{char} : {score}点（{percent:.1f}%）"
                )
