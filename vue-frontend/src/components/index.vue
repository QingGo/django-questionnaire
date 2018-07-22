<template>
<div class="container">
    <div class="index">
        <h2>问卷列表</h2>
        <div v-if="latest_questionnaire_list">
            <ul>
                <template v-for="questionnaire in latest_questionnaire_list">
                    <li :key=questionnaire.questionnaire_name>
                        <h4>
                            <a href=#>{{ questionnaire.questionnaire_name }}</a>
                        </h4>
                        <ul>
                            <template v-for="question in questionnaire.question_set">
                                <li :key=question.question_text> {{ question.question_text }}</li>
                            </template>
                        </ul>
                        <p>...</p>
                        <br/>
                        <p class="text-muted">问卷详情: {{ questionnaire.detail_info }}</p>
                        <small class="text-muted">发布日期: {{ questionnaire.pub_date }}
                                <a href=#>直接查看投票结果</a>
                        </small>
                    </li>
                </template>
            </ul>
        </div>
        <div v-else>
            <p>No polls are available.</p>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'index',
  data: function () {
    return {
      latest_questionnaire_list: []
    }
  },
  methods: {
    fetchQuestionnaire: function () {
      axios.get('http://127.0.0.1:8000/api/questionnaire/')
        .then((response) => {
        // 这里不写成函数式this好像无法正确指向，需弄清楚
          this.latest_questionnaire_list = response.data.questionnaire_list
        }, (error) => {
          console.log(error)
        })
    }
  },
  mounted: function () {
    this.fetchQuestionnaire()
  }
}
</script>
