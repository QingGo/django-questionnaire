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
                            <router-link :to="'result/' + questionnaire.id ">
                            直接查看投票结果
                            </router-link>
                        </small>
                    </li>
                    </div>
                </template>
                </transition-group>
            </ul>
            <button v-if="first_loaded && !all_loaded" @click="loadMore" id="more-info" class="btn btn-primary btn-block">加载更多</button>
            <div v-if="all_loaded" class="container pagination-container">
                <ul class="pagination">
                    <li :class="page-item" @click="changePage(1)"><router-link class="page-link" :to="{ name: 'index', query: { page: '1' }}">&laquo;</router-link></li>
                    <template v-for="page_index in pages_num">
                    <li :class="page-item" @click="changePage(page_index)" :key="page_index"><router-link class="page-link" :to="{ name: 'index', query: { page: page_index }}">{{ page_index }}</router-link></li>
                    </template>
                    <li :class="page-item" @click="changePage(pages_num)" ><router-link class="page-link" :to="{ name: 'index', query: { page: '2' }}">&raquo;</router-link></li>
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
axios.defaults.baseURL = 'http://' + process.env.BASE_URL
export default {
  name: 'index',
  data: function () {
    return {
      latest_questionnaire_list: [],
      pages_num: 0,
      loaded_num: 0,
      page: 1,
      first_loaded: false,
      all_loaded: false
    }
  },
  methods: {
    fetchQuestionnaire: function (refresh = false) {
      axios.get('/polls/api/questionnaires/?start=' + (this.loaded_num + 1) + '&page=' + this.page)
        .then((response) => {
          if (refresh) {
            this.pages_num = response.data.pages_num
            console.log(this.pages_num)
            this.latest_questionnaire_list = response.data.polls
            this.loaded_num = this.latest_questionnaire_list.length
            this.first_loaded = true
            this.all_loaded = false
          } else {
            this.latest_questionnaire_list = this.latest_questionnaire_list.concat(response.data.polls)
            this.loaded_num = this.latest_questionnaire_list.length
            this.first_loaded = true
            if (this.loaded_num > 10 || response.data.polls.length === 0) {
              this.all_loaded = true
            }
          }
        }, (error) => {
          console.log(error)
          this.all_loaded = true
        })
    },
    loadMore: function () {
      this.fetchQuestionnaire()
    },
    changePage: function (page) {
      console.log('change age: ' + page)
      this.page = page
      this.loaded_num = 0
      this.fetchQuestionnaire({refresh: true})
    }
  },
  mounted: function () {
    this.fetchQuestionnaire({refresh: true})
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
