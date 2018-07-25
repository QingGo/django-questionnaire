<template>
<div class="detail">
    <div class="container">
        <div id="questionnaire-info">
            <h2>{{ questions_list.questionnaire_name }}</h2>
            <small class="text-muted">发布日期: {{ questions_list.pub_date }}</small>
            <p class="text-muted">问卷详情: {{ questions_list.detail_info }}</p>
            <div v-if="error_info" class="alert alert-warning">你还未选完所有的选项!</div>
        </div>
    <div class="charts">
        <div id="myHistChart" :style="{width: '1000px', height: '700px'}"></div>
    </div>
    <ul>
        <template v-for="(question, question_index) in questions_list.question_set">
        <div class="row" :key=question.question_text>
            <div class="col-xs-6 col-sm-4" >
                <li>
                    <p>{{ question_index + 1 }}. {{ question.question_text }} </p>
                    <ul>
                    <template v-for="choice in question.choice_set">
                        <li :key=choice.choice_text> {{ choice.choice_text }} -- {{ choice.votes }} vote</li>
                    </template>
                    </ul>
                </li>
            </div>
            <div class="col-xs-6 col-sm-8">
                <div class="charts" id="myPieCharts">
                    <div :id="'myPieChart' + (question_index + 1)" :style="{width: '800px', height: '400px'}"></div>
                </div>
            </div>
        </div>
        </template>
    </ul>
    <router-link class="btn btn-primary btn-lg " :to="'/polls'">
        继续投票
    </router-link>
    </div>
</div>
</template>

<script>
import axios from 'axios'
let echarts = require('echarts/lib/echarts')
require('echarts/lib/chart/pie')
require('echarts/lib/chart/bar')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/title')
require('echarts/lib/component/legend')
export default {
  name: 'result',
  data: function () {
    return {
      questions_list: [],
      error_info: false,
      echarts_data: {
        'hist_data': {x: [], y: []},
        'pie_data': []},
      myPieChartDivs: []

    }
  },
  methods: {
    fetchQuestions: function () {
      axios.get('http://127.0.0.1:8000/polls/api/questionnaires/' + (this.$route.params.id))
        .then((response) => {
          this.questions_list = response.data
          this.perpareEchartsData()
          this.plotEcharts()
        }, (error) => {
          console.log(error)
        })
    },
    perpareEchartsData: function () {
      console.log(this.questions_list)
      for (let question of this.questions_list.question_set) {
        let onePieData = []
        for (let choice of question.choice_set) {
          this.echarts_data.hist_data.x.push(choice.choice_text)
          this.echarts_data.hist_data.y.push(choice.votes)
          onePieData.push({value: choice.votes, name: choice.choice_text})
        }
        this.echarts_data.pie_data.push(onePieData)
      }
      console.log(this.echarts_data)
    },
    plotEcharts: function () {
      let myHistChart = echarts.init(document.querySelector('#myHistChart'))
      myHistChart.setOption({
        title: {
          text: '投票结果总览'
        },
        xAxis: {
          data: this.echarts_data.hist_data.x
        },
        yAxis: {},
        series: [{
          name: '投票数',
          type: 'bar',
          data: this.echarts_data.hist_data.y
        }]
      })
      this.$nextTick(function () {
        this.myPieChartDivs = document.querySelectorAll('div#myPieCharts > div')
        for (let divIndex in this.myPieChartDivs) {
          let myPieCharts = echarts.init(this.myPieChartDivs[divIndex])
          console.log(this.echarts_data.pie_data[divIndex])
          myPieCharts.setOption({
            title: {
              text: '各选项所占百分比'
            },
            series: [
              {
                name: '各选项所占百分比',
                type: 'pie',
                radius: ['50%', '70%'],
                data: this.echarts_data.pie_data[divIndex]
              }
            ]
          })
        }
      })
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
