{% extends "index.html" %}

{% block content %}

<div class="cover4">
    <div class="card">
        <h2 class="card-title"> 1화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

 </p>
    </div>
    <div class="card">
        <h2 class="card-title"> 2화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

윤지는 매점남을 통해 근석이가 자기를 좋아한단 사실을 알게됩니
다. 그러나 정작 근석이는 아니라며 발뺌을 합니다. 아무래도 쑥스
러운가 보죠? 결국 윤지는 중철이와 짜고 근석이 마음을 떠보기로
하는데... </p>
    </div>

    <div class="card">
        <h2 class="card-title"> 3화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

윤지는 매점남을 통해 근석이가 자기를 좋아한단 사실을 알게됩니
다. 그러나 정작 근석이는 아니라며 발뺌을 합니다. 아무래도 쑥스
러운가 보죠? 결국 윤지는 중철이와 짜고 근석이 마음을 떠보기로
하는데... </p>
    </div>

    <div class="card">
        <h2 class="card-title"> 4화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

윤지는 매점남을 통해 근석이가 자기를 좋아한단 사실을 알게됩니
다. 그러나 정작 근석이는 아니라며 발뺌을 합니다. 아무래도 쑥스
러운가 보죠? 결국 윤지는 중철이와 짜고 근석이 마음을 떠보기로
하는데...</p>
    </div>

    <div class="card">
        <h2 class="card-title"> 5화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

윤지는 매점남을 통해 근석이가 자기를 좋아한단 사실을 알게됩니
다. 그러나 정작 근석이는 아니라며 발뺌을 합니다. 아무래도 쑥스
러운가 보죠? 결국 윤지는 중철이와 짜고 근석이 마음을 떠보기로
하는데... </p>
    </div>

    <div class="card">
        <h2 class="card-title"> 6화</h2>
        <p> 불어오는 가을바람에 왠지 마음이 허전한 승은이. 게다가 주변의
닭살 커플들이 염장을 질러댑니다. 커플들에게 이용만 당하느라
화가 잔뜩 난 승은이, 결국 주변의 커플들을 갈라놓기로 작정하는
데...

윤지는 매점남을 통해 근석이가 자기를 좋아한단 사실을 알게됩니
다. 그러나 정작 근석이는 아니라며 발뺌을 합니다. 아무래도 쑥스
러운가 보죠? 결국 윤지는 중철이와 짜고 근석이 마음을 떠보기로
하는데...</p>
    </div>

</div>



{% endblock %}




let rows = response["previews"]

            for(let i=0; i<rows.length; i++){

                let ContentNumber = rows[i]['ContentNumber']
                let Preview = rows[i]['Preview']
                let temp_html = ``

                temp_html = `<div class="card">
                                <h2 class="card-title"> ${ContentNumber}화</h2>
                                <p> ${Preview} </p>
                             </div>`

                $('#card-list').append(temp_html)