<template>
  <div id="backgroundcolor">
    <div class="text-center">
      <div class="header">
        <VueHeader
          :VueHeaderTitle="VueHeaderTitle"
          :VueHeaderContent="VueHeaderContent"
        />
      </div>
      <div class="body">
        <div id="form">
          <b-form
            @submit.prevent.stop="onSubmit"
            id="input-form"
            name="input-form"
          >
            <b-container>
              <!-- 닉네임 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-nickname">닉네임:</label>
                </b-col>
                <b-col sm="10">
                  <b-input-group>
                    <b-form-input
                      id="input-nickname"
                      ref="nickname"
                      v-model="form.nickname"
                      :state="validationNickname"
                      required
                    ></b-form-input>
                    <b-input-group-append
                      ><b-button
                        id="dupNicknameCheck"
                        v-on:click="duplicatedNicknameCheck"
                        >중복확인</b-button
                      ></b-input-group-append
                    >
                  </b-input-group>
                  <b-form-invalid-feedback :state="validationNickname">
                    {{ validationNicknameMsg }}
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="validationNickname">
                    사용 가능한 닉네임입니다.
                  </b-form-valid-feedback>
                </b-col>
              </b-row>

              <!-- 나이 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-age">나이:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-input
                    id="input-age"
                    ref="age"
                    type="number"
                    :state="validationAge"
                    v-model="form.age"
                    required
                  ></b-form-input>
                  <b-form-invalid-feedback :state="validationAge">
                    나이를 입력해주세요.
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="validationAge">
                    OK!
                  </b-form-valid-feedback>
                </b-col>
              </b-row>

              <!-- 성별 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-gender">성별:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-radio-group
                    id="radio-group-gender"
                    v-model="form.gender"
                    :options="optionsGender"
                    buttons
                    size="sm"
                  ></b-form-radio-group>
                </b-col>
              </b-row>

              <!-- 키 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-height">키:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-input
                    id="input-height"
                    ref="height"
                    type="number"
                    step="any"
                    v-model="form.height"
                    :state="validationHeight"
                    required
                  ></b-form-input>
                  <b-form-invalid-feedback :state="validationHeight">
                    키를 입력해주세요.
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="validationHeight">
                    OK!
                  </b-form-valid-feedback>
                </b-col>
              </b-row>

              <!-- 체중 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-weight">체중:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-input
                    id="input-weight"
                    ref="weight"
                    type="number"
                    step="any"
                    :state="validationWeight"
                    v-model="form.weight"
                    required
                  ></b-form-input>
                  <b-form-invalid-feedback :state="validationWeight">
                    체중을 입력해주세요.
                  </b-form-invalid-feedback>
                  <b-form-valid-feedback :state="validationWeight">
                    OK!
                  </b-form-valid-feedback>
                </b-col>
              </b-row>

              <!-- 기종 --->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-phone-type">휴대폰 기종:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-radio-group
                    id="radio-group-phone-type"
                    v-model="form.phoneType"
                    :options="optionsPhoneType"
                    size="sm"
                    buttons
                  ></b-form-radio-group>
                </b-col>
              </b-row>

              <!-- 공개여부 -->
              <b-row class="my-5">
                <b-col sm="2">
                  <label for="input-user-public">정보 공개 여부:</label>
                </b-col>
                <b-col sm="10">
                  <b-form-radio-group
                    id="input-user-public"
                    v-model="form.userPublic"
                    :options="publics"
                    buttons
                    size="sm"
                  ></b-form-radio-group>
                </b-col>
              </b-row>

              <!-- 캐릭터 선택 -->
              <b-row>
                  <b-col sm="2">
                    <label for="input-avatar">아바타:</label>
                  </b-col>
                  <b-col sm="10">
                    <b-row cols="5">
                      <div 
                        v-for="(index) in 10" 
                        :key="index">
                        <b-col class="div-avatar"> 
                          <input type="radio" :id="`select-avatar${ index }`" class="test-avatar" name="select-avatar" v-model="form.userAvatar" :value="`avatar${index}`">
                          <label :for="`select-avatar${ index }`" class="label-avatar">
                            <div class="div-img-avatar">
                              <img :src="require(`/public/user-avatar/avatar${index}.png`)" id="img-avatar">
                            </div>
                          </label>
                        </b-col>
                      </div>
                    </b-row>
                  </b-col>
              </b-row>

              <b-row class="my-5">
                <b-col sm="2"></b-col>
                <b-col sm="10">
                  <b-button type="submit" variant="primary">완료!</b-button>
                </b-col>
              </b-row>
            </b-container>
          </b-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import VueHeader from "@/components/common/VueHeader.vue";
import axios from "axios";
import { mapGetters, mapMutations } from "vuex";

const SERVER_URL = "https://j8b106.p.ssafy.io/api/users";
// const SERVER_URL = "http://localhost:8085/users";

export default {
  name: "ExtraInfoFormView",

  components: {
    VueHeader,
  },

  data() {
    return {
      VueHeaderTitle: "VITA에 오신 것을 환영합니다!",
      VueHeaderContent: "서비스 사용을 위해 추가 정보를 입력해주세요.",

      form: {
        nickname: "",
        age: 0,
        height: 0,
        weight: 0,
        gender: "male",
        phoneType: "SAMSUNG",
        userPublic: true,
        userAvatar: "avatar1"
      },
      optionsGender: [
        { text: "남자", value: "male" },
        { text: "여자", value: "female" },
      ],
      optionsPhoneType: [
        { text: "삼성", value: "SAMSUNG" },
        { text: "애플", value: "APPLE" },
      ],
      publics: [
        { text: "public", value: true },
        { text: "private", value: false },
      ],
      show: true,
      isCheckNickname: false,
      isDupNickname: true,
      validationNicknameMsg: "",
      selectedAvatar: "avatar1",
    };
  },

  computed: {
    ...mapGetters(["token", "user"]),

    validationNickname() {
      if (this.form.nickname.length > 0) {
        this.validationNicknameMsg = "닉네임 중복검사를 해주세요.";
        if (this.isDupNickname == false && this.isCheckNickname == true) {
          this.validationNicknameMsg = "사용 가능한 닉네임입니다.";
          return true;
        } else if (this.isDupNickname == true && this.isCheckNickname == true) {
          this.validationNicknameMsg = "중복된 닉네임입니다.";
          return false;
        }
        return false;
      }
      this.validationNicknameMsg = "닉네임을 입력해주세요.";
      return false;
    },

    validationAge() {
      return this.form.age > 0 && this.form.age < 150;
    },

    validationHeight() {
      return this.form.height > 0;
    },

    validationWeight() {
      return this.form.weight > 0;
    },
  },

  methods: {
    onSubmit(event) {
      event.preventDefault();

      if (
        this.form.nickname.value == "" ||
        this.isCheckNickname == false ||
        this.isDupNickname == true
      ) {
        this.$refs.nickname.focus();
        return false;
      }
      if (this.form.age == 0) {
        this.$refs.age.focus();
        return false;
      }
      if (this.form.height == 0) {
        this.$refs.height.focus();
        return false;
      }
      if (this.form.weight == 0) {
        this.$refs.weight.focus();
        return false;
      }

      axios
        .put(
          SERVER_URL + `/extrainfo`,
          {
            nickname: this.form.nickname,
            age: this.form.age,
            height: this.form.height,
            weight: this.form.weight,
            gender: this.form.gender,
            phoneType: this.form.phoneType,
            userPublic: this.form.userPublic,
            userAvatar: this.form.userAvatar,
          },
          {
            headers: {
              'Authorization': `Bearer ${this.token}`,
            },
          }
        )
        .then((response) => {
          if (response.status == 200) {
            this.setUserNickname(this.form.nickname);
            this.$router.replace("/fileupload");
          }
        });
    },

    duplicatedNicknameCheck() {
      axios
        .get(SERVER_URL + `/search/nickname?nickname=` + this.form.nickname)
        .then((response) => {
          if (response.status == 200) {
            if (response.data.body.isDupNickname == "true") {
              this.isDupNickname = true;
              this.isCheckNickname = true;
            } else {
              this.isDupNickname = false;
              this.isCheckNickname = true;
            }
          }
        });
    },
    ...mapMutations(['setUserNickname'])
  },
};
</script>

<style scoped>
#backgroundcolor {
  background: linear-gradient(
      146.55deg,
      rgba(174, 162, 220, 0.2) -70.09%,
      rgba(140, 112, 253, 0) 55.52%
    ),
    linear-gradient(
      0deg,
      rgba(243, 255, 228, 0.2) -26.8%,
      rgba(178, 215, 149, 0.012) 16.1%,
      rgba(220, 243, 253, 0) 131.6%
    ),
    linear-gradient(239.1deg, #e2faff -29.57%, rgba(222, 243, 248, 0) 131.52%);
  /* height: 1000vh; */
  overflow: hidden;
  margin: 0;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}
.body {
  display: flex;
  justify-content: center;
}

#form {
  width: 60%;
  background: #ffffffcc;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 20px;
  margin: 1rem;
  color: rgb(0, 0, 0);
  display: flex;
  justify-content: space-around;
  align-items: center;
}

#input-form {
  width: 90%;
}

label {
  float: right;
  font-weight: 600;
  color: #172176;
}

#dupNicknameCheck {
  margin-left: 20px;
}

#img-avatar {
  width: 120px;
  height: 180px; 
  object-fit: contain;
}

.div-avatar input[type=radio] {
  display: none;
}

.div-avatar input[type=radio]:checked +label #img-avatar{
    border: 3px solid gold;
    border-radius: 10px;
}
</style>