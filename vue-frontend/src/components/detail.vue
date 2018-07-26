<template>
<div class="detail">
    <div class="container">
        <div id="questionnaire-info">
            <h2>{{ questions_list.questionnaire_name }}</h2>
            <small class="text-muted">发布日期: {{ questions_list.pub_date }}</small>
            <p class="text-muted">问卷详情: {{ questions_list.detail_info }}</p>
            <div v-if="error_info" class="alert alert-warning">你还未选完所有的选项!</div>
        </div>
        <form role="form" method="POST">
            <template v-for="(question, question_index) in questions_list.question_set">
                <div class="form-group" :key=question.question_text>
                <p>{{ question_index + 1 }}. {{ question.question_text }} </p>
                <template v-for="choice in question.choice_set">
                    <el-radio v-model="question.picked" :label="choice.id" :key="choice.choice_text">
                      {{ choice.choice_text }}
                    </el-radio>
                </template>
                </div>
            </template>
        </form>
        <button class="btn btn-primary btn-lg" @click="mySubmit">提交</button>
        <router-link class="btn btn-primary btn-lg " :to="'/polls'">
            回到问卷列表
        </router-link>
        <router-link class="btn btn-primary btn-lg " :to="'/result/' + questions_list.id ">
            直接查看投票结果
        </router-link>

    </div>
</div>
</template>

<script>
import axios from 'axios'
axios.defaults.baseURL = 'http://' + process.env.BASE_URL
export default {
  name: 'detail',
  data: function () {
    return {
      questions_list: [],
      error_info: false
    }
  },
  methods: {
    fetchQuestions: function () {
      axios.get('/polls/api/questionnaires/' + (this.$route.params.id))
        .then((response) => {
        // 这里不写成函数式this好像无法正确指向，需弄清楚
          console.log(response.data)
          this.questions_list = response.data
        }, (error) => {
          console.log(error)
        })
    },
    mySubmit: function () {
      this.error_info = false
      for (let question of this.questions_list.question_set) {
        this.error_info = this.error_info || !question.picked
      }
      if (this.error_info) {
        console.log('not all selected')
      } else {
        axios.put('/polls/api/questionnaires/' + (this.$route.params.id) + '/', this.questions_list)
          .then((response) => {
            this.$router.push({
              name: 'result',
              params: { id: this.$route.params.id
              }})
          }, (error) => {
            console.log(error)
          })
      }
    }
  },
  mounted: function () {
    this.fetchQuestions()
  }
}
</script>

<style scoped>
div#questionnaire-info{
    margin-top: 10px;
    margin-bottom: 20px;
}
</style>
