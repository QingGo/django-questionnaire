<template>
<div class="container">
    <div class="index">
        <div v-if="latest_questionnaire_list">
            <ul>
                <transition-group name="fade">
                <template v-for="questionnaire in latest_questionnaire_list">
                    <div class="questionnaire_block" :key=questionnaire.questionnaire_name>
                    <li>
                        <h4>
                            <router-link :to="'detail/' + questionnaire.id ">
                            {{ questionnaire.questionnaire_name }}
                            </router-link>
                        </h4>
                        <ul>
                            <template v-for="question in questionnaire.question_set">
                                <li :key=question.question_text> {{ question.question_text }}</li>
                            </template>
                        </ul>
                        <p>...</p>
                        <p class="text-muted">问卷详情: {{ questionnaire.detail_info }}</p>
                        <small class="text-muted">发布日期: {{ questionnaire.pub_date }}
                            <router-link :to="'results/' + questionnaire.id ">
                            直接查看投票结果
                            </router-link>
                        </small>
                        <br>
                        <br>
                    </li>
                    </div>
                </template>
                </transition-group>
            </ul>
            <button v-if="first_loaded" @click="loadMore" id="more-info" class="btn btn-primary btn-block">加载更多</button>
            <div v-if="all_loaded" class="container pagination-container">
                <ul class="pagination">
                    <li class="page-item"><a class="page-link" href="#">&laquo;</a></li>
                    <li class="page-item"><a class="page-link" href="#">1</a></li>
                    <li class="page-item"><a class="page-link" href="#">2</a></li>
                    <li class="page-item"><a class="page-link" href="#">&raquo;</a></li>
                </ul>
            </div>
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
      latest_questionnaire_list: [],
      loaded_num: 0,
      first_loaded: false,
      all_loaded: false
    }
  },
  methods: {
    fetchQuestionnaire: function () {
      axios.get('http://127.0.0.1:8000/polls/api/questionnaires/?start=' + (this.loaded_num + 1))
        .then((response) => {
        // 这里不写成函数式this好像无法正确指向，需弄清楚
          this.latest_questionnaire_list = this.latest_questionnaire_list.concat(response.data)
          this.loaded_num += 5
          this.first_loaded = true
          if (this.loaded_num > 10) {
            this.all_loaded = true
          }
        }, (error) => {
          console.log(error)
          this.all_loaded = true
        })
    },
    loadMore: function () {
      this.fetchQuestionnaire()
    }
  },
  mounted: function () {
    this.fetchQuestionnaire()
  }
}
</script>

<style scoped>
div.questionnaire_block {
    padding: 16px 30px;
    margin: 10px;
    background: #fff;
    overflow: hidden;
    border-radius: 2px;
    box-shadow: 0px 0px 10px rgba(26,26,26,.3);
    box-sizing: border-box;
    display: block;
    background-color: antiquewhite;
}
div.pagination-container {
    margin-top: 30px;
    margin-left: 30px;
}
</style>
