<template>
  <div>
    <ComponentHeader
      :ComponentHeaderTitle="ComponentHeaderTitle"
      :ComponentHeaderContent="ComponentHeaderContent"
    />
    <div id="rhr-middle">
      <div id="rhr-middle-left-btn">
        <div id="rhr-middle-left-btn-up">
          <input type="radio" name="rhr-period" id="rhr-week" value="week" v-on:click="weekRhr" checked>
          <label for="rhr-week">일별</label>

          <input type="radio" name="rhr-period" id="rhr-month" value="month" v-on:click="monthRhr">
          <label for="rhr-month">주별</label>

          <input type="radio" name="rhr-period" id="rhr-year" value="year" v-on:click="yearRhr">
          <label for="rhr-year">월별</label>
          <div>
            <img @click="info()" style="width: 18%" src="@/../public/wearable/question.png" />
          </div>
        </div>
        <div id="rhr-middle-left-btn-down">
          <div style="font-size: 18px; font-rhr: 800; color: #5b5a63">
            심박수
          </div>
          <div style="font-size: 18px; font-rhr: 800; color: #5b5a63">
            종합점수
          </div>
          <div style="
              font-size: 60px;
              margin-top: -0.8rem;
              font-rhr: 800;
              color: #5b5a63;">
            {{ score }}
          </div>
        </div>
      </div>
      <div id="rhr-middle-left">
        <!-- 그래프 그려지는 곳 -->
        <!-- <div id="rhrchart"></div> -->
        <div v-if="data.length == 0">
          <img :src="require(`/public/wearable/no_data_found.png`)" id="no_data_found" width="200px">
          <p> 표시할 심박변이 데이터가 없습니다 <br>
              tip : 심박수 측정을 활성화하여 데이터를 입력해주세요 </p>
        </div>
        <div v-else>
          <RhrChart :key="componentKey" :date="date" :data="data" />
        </div>
        
        <div v-if="infovalue" id="rhr-middle-left-child">측정된 심박수 평균을 표시합니다.</div>
      </div>
      <div id="rhr-middle-right">
        <div id="rhr-middle-right-div">
          <div v-if="past.weekNowWearableRhr < past.weekPastWearableRhr">
            <p id="rhr-middle-right-div-h">이번 주 평균 심박수가 지난주보다 감소했습니다</p>
          </div>
          <div v-else-if="past.weekNowWearableRhr == past.weekPastWearableRhr">
            <p id="rhr-middle-right-div-h">이번 주 평균 심박수는 지난주와 동일합니다</p>
          </div>
          <div v-else>
            <p id="rhr-middle-right-div-h">이번 주 평균 심박수가 지난주보다 감소했습니다</p>
          </div>
          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">이번 주</span>
            <div class="progress col-9 px-0" id="weekNowWearableRhr">
              <div
                id="rhr-week-now-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.weekNowWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.weekNowPersent }"
              >
                <span id="rhr-now-progress-p" class="sr-only">{{
                  past.weekNowWearableRhr
                }}</span>
              </div>
            </div>
          </div>

          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">지난주</span>
            <div class="progress col-9 px-0" id="weekPastWearableRhr">
              <div
                id="rhr-past-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.weekPastWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.weekPastPersent }"
              >
                <span id="rhr-progress-p" class="sr-only">{{
                  past.weekPastWearableRhr
                }}</span>
              </div>
            </div>
          </div>
        </div>

        <div id="rhr-middle-right-div">
          <div v-if="past.monthNowWearableRhr < past.monthPastWearableRhr">
            <p id="rhr-middle-right-div-h">이번 달 평균 심박수가 지난달보다 감소했습니다</p>
          </div>
          <div v-else-if="past.monthNowWearableRhr == past.monthPastWearableRhr">
            <p id="rhr-middle-right-div-h">이번 달 평균 심박수는 지난달과 동일합니다</p>
          </div>
          <div v-else>
            <p id="rhr-middle-right-div-h">이번 달 평균 심박수가 지난달보다 증가했습니다</p>
          </div>
          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">이번 달</span>
            <div class="progress col-9 px-0" id="monthNowWearableRhr">
              <div
                id="rhr-month-now-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.monthNowWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.monthNowPersent }"
              >
                <span id="rhr-now-progress-p" class="sr-only">{{
                  past.monthNowWearableRhr
                }}</span>
              </div>
            </div>
          </div>

          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">지난달</span>
            <div class="progress col-9 px-0" id="monthPastWearableRhr">
              <div
                id="rhr-past-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.monthPastWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.monthPastPersent }"
              >
                <span id="rhr-progress-p" class="sr-only">{{
                  past.monthPastWearableRhr
                }}</span>
              </div>
            </div>
          </div>
        </div>

        <div id="rhr-middle-right-div">
          <div v-if="past.yearNowWearableRhr < past.yearPastWearableRhr">
            <p id="rhr-middle-right-div-h">올해 평균 심박수가 작년보다 감소했습니다</p>
          </div>
          <div v-else-if="past.yearNowWearableRhr == past.yearPastWearableRhr">
            <p id="rhr-middle-right-div-h">올해 평균 심박수는 작년과 동일합니다</p>
          </div>
          <div v-else>
            <p id="rhr-middle-right-div-h">올해 평균 심박수가 작년보다 증가했습니다</p>
          </div>

          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">올해</span>
            <div class="progress col-9 px-0" id="yearNowWearableRhr">
              <div
                id="rhr-year-now-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.yearNowWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.yearNowPersent }"
              >
                <span id="rhr-now-progress-p" class="sr-only">{{
                  past.yearNowWearableRhr
                }}</span>
              </div>
            </div>
          </div>
          <div class="row">
            <span id="rhr-middle-right-div-p" class="col-2">작년</span>
            <div class="progress col-9 px-0" id="yearPastWearableRhr">
              <div
                id="rhr-past-progess"
                class="progress-bar"
                role="progressbar"
                :aria-valuenow="past.yearPastWearableRhr"
                aria-valuemin="0"
                aria-valuemax="100"
                :style="{ width: past.yearPastPersent }"
              >
                <span id="rhr-progress-p" class="sr-only">{{
                  past.yearPastWearableRhr
                }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ComponentHeader from "@/components/common/ComponentHeader.vue";
import RhrChart from "@/components/wearable/RhrChart.vue";
import { mapGetters } from "vuex";

export default {
  name: "Wearablerhr",
  components: {
    ComponentHeader,
    RhrChart,
  },

  data: () => ({
    ComponentHeaderTitle: "심박변이",
    ComponentHeaderContent: "나의 심박변이 기록을 보여줘요.",
    data: [],
    date: [],
    past: [],
    // 설명란
infovalue:false,
    componentKey: 0,
  }),

  props: {
    score: Number,
  },

  // 데이터 가져오는 곳
  created() {
    this.weekRhr();
    this.pastAndNowRhr();
  },

  computed: {
    ...mapGetters(["token", "user"]),
  },
  
  methods: {
    info() { 
          if (this.infovalue == true) {
            this.infovalue = false;
          } else { 
            this.infovalue = true;
          }
    },
    async weekRhr() {
      await axios
        .get(this.$store.state.url + "rhr/daily", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((res) => {
          this.data = res.data.map(function (e) {
            return e.dailyWearableRhr;
          });
          this.date = res.data.map(function (e) {
            return e.date;
          });
          this.componentKey += 1;
        });
    },
    async monthRhr() {
      await axios
        .get(this.$store.state.url + "rhr/weekly", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((res) => {
          this.data = res.data.map(function (e) {
            return e.weeklyWearableRhr;
          });
          this.date = res.data.map(function (e) {
            return e.date;
          });
          this.componentKey += 1;
        });
    },
    async yearRhr() {
      await axios
        .get(this.$store.state.url + "rhr/monthly", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((res) => {
          this.data = res.data.map(function (e) {
            return e.monthlyWearableRhr;
          });
          this.date = res.data.map(function (e) {
            return e.date;
          });
          this.componentKey += 1;
        });
    },
    async pastAndNowRhr() {
      await axios
        .get(this.$store.state.url + "rhr/past", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${this.token}`,
          },
        })
        .then((res) => {
          this.past = res.data;
          if (this.past.weekPastWearableRhr >= this.past.weekNowWearableRhr) {
            this.past["weekNowPersent"] =
              (this.past.weekNowWearableRhr / this.past.weekPastWearableRhr) *
              100 +
              "%";
            this.past["weekPastPersent"] = 100 + "%";
          } else {
            this.past["weekNowPersent"] = 100 + "%";
            this.past["weekPastPersent"] =
              (this.past.weekPastWearableRhr / this.past.weekNowWearableRhr) *
                100 +
              "%";
          }
          if (this.past.monthPastWearableRhr >= this.past.monthNowWearableRhr) {
            this.past["monthNowPersent"] =
              (this.past.monthNowWearableRhr / this.past.monthPastWearableRhr) *
                100 +
              "%";
            this.past["monthPastPersent"] = 100 + "%";
          } else {
            this.past["monthNowPersent"] = 100 + "%";
            this.past["monthPastPersent"] =
              (this.past.monthPastWearableRhr / this.past.monthNowWearableRhr) *
                100 +
              "%";
          }
          if (this.past.yearPastWearableRhr >= this.past.yearNowWearableRhr) {
            this.past["yearNowPersent"] =
              (this.past.yearNowWearableRhr / this.past.yearPastWearableRhr) *
                100 +
              "%";
            this.past["yearPastPersent"] = 100 + "%";
          } else {
            this.past["yearNowPersent"] = 100 + "%";
            this.past["yearPastPersent"] =
              (this.past.yearPastWearableRhr / this.past.yearNowWearableRhr) *
                100 +
              "%";
          }
        });
    },
  },
};
</script>

<style scoped>
#rhr-week-now-progess {
  background: #3027e5;
  border-radius: 10px;
}

#rhr-month-now-progess {
  background: #27e58a;
  border-radius: 10px;
}

#rhr-now-progress-p {
  font-size: 0.8rem;
  font-weight: 600;
}

#rhr-progress-p {
  font-size: 0.8rem;
  font-weight: 600;
  color: black;
}

#rhr-year-now-progess {
  background: #f33249;
  border-radius: 10px;
}

#rhr-past-progess {
  background: #d0d6e5;
  border-radius: 10px;
}

#rhr-middle-right-div-p {
  font-size: 1rem;
  font-weight: 800;
  margin-left: -1rem;
}
#rhr-middle-right-div-h {
  font-size: 1rem;
  font-weight: 800;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

#rhr-middle {
  height: 400px;
  /* background-color: aqua; */
  margin: 3rem;
  display: flex;
  justify-content: center;
  align-items: center;
}
#rhr-middle-left-btn {
  width: 12%;
  height: 100%;
  /* display: flex; */
  /* justify-content: center;
  align-items: center; */
  /* background-color: rgb(255, 255, 255); */
}
#rhr-middle-left {
  width: 44%;
  height: 100%;
  align-items: center;
  background-color: rgb(255, 255, 255);
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  position: relative;
}
#rhr-middle-left-child{
  width: 100%;
  height: 100%;
  align-items: center;
  background-color: rgb(255, 255, 255);
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  /* 부모 */
  position: absolute;
    left: 0;
    top: 0;
    z-index: 9;
    opacity: 0.9;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
    font-size: 1.2rem;
    padding: 4rem;
    background-color: #bbe5f7;
    color:black;
}

#rhr-middle-right {
  margin-left: 2%;
  width: 42%;
  height: 100%;
  /* background-color: rgb(0, 0, 0); */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  /* align-items: center; */
}

input[type="radio"] {
  display: none;
}

input[type="radio"] + label {
  display: inline-block;
  width: 70%;
  height: 35px;
  border: none;
  color: rgb(255, 255, 255);
  font-weight: 600;
  background: #3695be;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 12px;
  margin-bottom: 1rem;
  text-align: center;
  line-height: 35px;
}

input[type="radio"]:checked + label {
  width: 70%;
  height: 35px;
  border: none;
  color: #3695be;
  border: solid 2px #3695be;
  font-weight: 600;
  background: rgb(255, 255, 255);
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 12px;
  cursor: pointer;
}

input[type="radio"]:hover + label {
  cursor: pointer;
}

#rhr-middle-left-btn-up {
  height: 70%;
}
#rhrchart {
  width: 150%;
  height: 90%;
  margin-top: 1rem;
  /* margin: auto; */
}
#rhr-middle-right-div {
  width: 100%;
  height: 28%;
  background: #ffffff;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;

  /* display: flex; 
flex-direction: column;
justify-content: space-between; */
}
.row {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: 0;
}
</style>