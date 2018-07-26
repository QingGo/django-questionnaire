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
axios.defaults.baseURL = 'http://' + process.env.BASE_URL
let echarts = require('echarts/lib/echarts')
require('echarts/lib/chart/pie')
require('echarts/lib/chart/bar')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/title')
require('echarts/lib/component/legend')
require('echarts/lib/component/markPoint')
require('echarts/lib/component/markLine')
export default {
  name: 'result',
  data: function () {
    return {
      questions_list: [],
      error_info: false,
      echarts_data: {
        hist_data: {x: [], y: []},
        pie_data: {data: [], legends: []}},
      myPieChartDivs: []

    }
  },
  methods: {
    fetchQuestions: function () {
      axios.get('/polls/api/questionnaires/' + (this.$route.params.id))
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
        let onePieLegends = []
        for (let choice of question.choice_set) {
          this.echarts_data.hist_data.x.push(choice.choice_text)
          this.echarts_data.hist_data.y.push(choice.votes)
          onePieData.push({value: choice.votes, name: choice.choice_text})
          onePieLegends.push(choice.choice_text)
        }
        this.echarts_data.pie_data.data.push(onePieData)
        this.echarts_data.pie_data.legends.push(onePieData)
      }
      console.log(this.echarts_data)
    },
    plotEcharts: function () {
      let myHistChart = echarts.init(document.querySelector('#myHistChart'))
      myHistChart.setOption({
        title: {
          text: '投票结果总览'
        },
        toolbox: {
          show: true,
          orient: 'vertical',
          left: '95%',
          top: 'center',
          feature: {
            saveAsImage: {
              show: true,
              title: '下载图片'
            },
            restore: {
              show: true
            },
            dataView: {
              show: true
            }
          }
        },
        tooltip: {
          trigger: 'item',
          triggerOn: 'mousemove|click',
          axisPointer: {
            type: 'line'
          },
          textStyle: {
            fontSize: 14
          },
          backgroundColor: 'rgba(50,50,50,0.7)',
          borderColor: '#333',
          borderWidth: 0
        },
        xAxis: {
          data: this.echarts_data.hist_data.x,
          axisLabel: {rotate: 30}
        },
        yAxis: {},
        series: [{
          name: '投票数',
          type: 'bar',
          data: this.echarts_data.hist_data.y,
          markPoint: {
            data: [
              {type: 'max', name: '最大值'},
              {type: 'min', name: '最小值'}
            ]
          },
          markLine: {
            data: [
              {type: 'average', name: '平均值'}
            ]
          }
        }]
      })
      this.$nextTick(function () {
        this.myPieChartDivs = document.querySelectorAll('div#myPieCharts > div')
        for (let divIndex in this.myPieChartDivs) {
          let myPieCharts = echarts.init(this.myPieChartDivs[divIndex])
          myPieCharts.setOption({
            title: {
              text: '各选项所占百分比'
            },
            tooltip: {
              trigger: 'item',
              triggerOn: 'mousemove|click',
              axisPointer: {
                type: 'line'
              },
              textStyle: {
                fontSize: 14
              },
              backgroundColor: 'rgba(50,50,50,0.7)',
              borderColor: '#333',
              borderWidth: 0
            },
            legend: [
              {
                data: this.echarts_data.pie_data.legends[divIndex],
                selectedMode: 'multiple',
                show: true,
                left: 'center',
                top: 'top',
                orient: 'horizontal',
                textStyle: {
                  fontSize: 12
                }
              }
            ],
            series: [
              {
                name: '各选项所占百分比',
                type: 'pie',
                radius: ['30%', '75%'],
                data: this.echarts_data.pie_data.data[divIndex]
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
