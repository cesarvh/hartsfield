<Suspense>
<template>
  <v-container>
    <v-responsive>
      Welcome {{ user.userName }}
      <div v-if="user.isAdmin">
        <p>Search a student's archives:</p>
        <v-row>
          <v-col>
            <v-text-field 
            clearable
            placeholder="Datahub folder link:  gs://ucb-datahub-archived-homedirs/..."
          /> 
        
          </v-col>
          <v-col cols="2">
            <v-btn
            @click="getUserUrls()"
          >
          Search
          </v-btn>

          </v-col>
          <v-col cols="2">
            <v-btn
              @click="clearResults()"
            >Clear</v-btn>
          </v-col>

        </v-row>
      </div>      

      <div v-if="userUrls.length">
        <div v-for="url in userUrls">
          <v-row>
            <v-col>
              {{url.signed_url}}
              <input type="hidden" id="signed-url" :value="url.signedUrl">
            </v-col>
            <v-col>
              {{url.expiration_date}}
            </v-col>
            <v-col>
              <v-btn 
                @click="copyUrl(url.signed_url)"
              >
                Copy
              </v-btn>
            </v-col>
          </v-row>
        </div>

      </div>
    </v-responsive>
  </v-container>
</template>
</Suspense>




<script>
import axios from 'axios';

export default {
  name: 'Profile',
  data:() => ({
    user: {},
    userUrls: [],
  }),
  async setup() {
    const path = "http://127.0.0.1:5000/api/account"
    console.log("hi")
    axios.get(path)
    .then((res) => {
      this.user = res;
    }).catch((err) =>{
      console.log(err)
    })
  },
  methods: {
    getUserUrls() {
      const path = "http://127.0.0.1:5000/api/user/1/url"
      axios.get(path)
      .then((res) => {
        this.userUrls = res.data;
        console.log(res)
      }).catch((err) => {
        console.log(err)
      })   
    },
    clearResults() {
      this.userUrls = []
    },
    copyUrl() {
      // TO DO: Copy Logic
    }
  },
}
</script>
