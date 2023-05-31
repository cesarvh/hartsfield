<template>
  <v-container>
    <v-responsive>
      <div class="text-h5 mt-5">Welcome {{ user.userName }}</div>
      <div v-if="user.isAdmin" class="pt-5">
        <p class="pb-4">Search a user's archives:</p>
        <v-row>
          <v-col>
            <v-text-field
            v-model="searchQuery"
            clearable
            placeholder="Please enter a Datahub Archive Link"
            id="archive-searchbox"
          /> 
        
          </v-col>
          <v-col cols="2">
            <v-btn
            class="mt-2 ml-10"
            @click="fetchSingleUrl"
          >
          Search
          </v-btn>

          </v-col>
          <v-col cols="2">
            <v-btn
              class="mt-2"
              @click="clearResults"
            >Clear</v-btn>
          </v-col>

        </v-row>
      </div>
      
      <div v-else class="align-center text-center p5">
        <v-btn 
          class="mt-10 mb-5 ml-10"
          size="large"
          rounded="xs"
          color="blue"
          @click="fetchAllUrls"
          >
            Retrieve my archives
        </v-btn>
      </div>

      <div v-if="userUrls.length">
        <v-table>
          <thead>
            <tr>
              <th class="text-left">
                Hub
              </th>
              <th class="text-left">
                Days Until Archived
              </th>
              <th class="text-left">
                URL
              </th>
              <th class="text-left">
                Actions
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(url, index) in userUrls"
              :key="index"
            >
              <td>{{ url.class_name }}</td>
              <td :id="`clone-${index}`">{{ getDayDifference(url.expiration_date) }}</td>
              <td>{{ url.signed_url }}</td>
              <td>              
                <v-btn
                  size="small"
                  @click="copyUrl(url.signed_url)"
                >
                  Copy
                </v-btn>
              </td>
            </tr>
          </tbody>
        </v-table>

      </div>

      
      <div v-if="error" class="align-center text-center pt-5">
          The requested user does not exist, or an invalid URL was provided.
      </div>
    </v-responsive>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Profile',
  data:() => ({
    user: {
    },
    error: false,
    searchQuery: '',
    userDetails: {},
    userUrls: [],
  }),
  methods: {
    clearResults() {
      this.userUrls = []
      this.error = false
    },
    copyUrl(signedUrl) {
      const input = document.createElement('textarea')

      if (this.userUrls.length <= 1) {
        input.value = `Below is a signed URL good for 7 days that you can use to retrieve your files: \n\n${signedUrl}`
      } else {
        input.value = signedUrl
      }
      document.body.appendChild(input)
      input.select()
      document.execCommand('copy')
      document.body.removeChild(input)

      console.log(`Copied ${signedUrl} to clipboard`)
    },
    fetchSingleUrl() {
      this.error = false
      let query = this.searchQuery

      query = query.substring(
                query.indexOf('datahub/') + "datahub/".length, 
                query.indexOf(".tar.gz"))
      const path = `http://127.0.0.1:5000/api/user/${query}/url`

      axios.get(path)
      .then((res) => {
        if (!res.data.length) {
          this.error = true
        } else {
          this.userUrls = res.data;
        }
      }).catch((err) => {
        this.error = true
        console.log(err)
      })   
    },
    fetchAllUrls(){
      const path = `http://127.0.0.1:5000/api/user/${this.user.uid}/urls`
      axios.get(path)
      .then((res) => {
        this.userUrls = res.data;
      }).catch((err) => {
        this.error = true
        console.log(err)
      })   
    },
    getAccountDetails() {
      const path = "http://127.0.0.1:5000/api/account"
      axios.get(path).then((res) => {
        this.user = res.data;
      }).catch((err) => {
        console.log(err)
      })
    },
    getDayDifference(date) {
      const today = new Date()
      const expDate = new Date(date)
      const diffInMilliseconds = Math.abs(today - expDate)

      return Math.ceil(diffInMilliseconds / (1000 * 60 * 60 *24))
    }
  },
  beforeMount() {
    this.getAccountDetails()
  },
}
</script>

<style>
td {
  white-space: nowrap; 
  text-overflow:ellipsis; 
  overflow: hidden; 
  max-width:275px;
}

</style>
