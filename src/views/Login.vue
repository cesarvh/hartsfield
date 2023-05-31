<template>
<v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height ">
      <v-sheet
          border
          rounded
          :height="500"
          :width="400"
          class="frosted px-8 py-6 accent-border accent-text mx-auto "
      >
        <v-img src="@/assets/berkeleylogo.png"></v-img>    
        <p class="my-5  text-h5 font-weight-light" >
            Welcome to the DataHub Archive Retrieval Tool
        </p>
        <v-btn 
          class="my-5 font-weight-light"
          :to="{ name: 'Urls' }"
          size="x-large"
          variant="flat"
          color="#3c7cc0"
          >
          Log In
        </v-btn>
        
        <p class="ma-5 pa-5 text-caption font-weight-light">
          Operated by the Division of Computing, Data Science, and Society
        </p>
      </v-sheet>
    </v-responsive>
  </v-container>
</template>

<script lang="ts">
import { RouterLink } from 'vue-router'

  export default{
    name: 'Login',
    components: {
      RouterLink,
    },
    methods: {
      toCasLogin() {
        console.log("Redirecting to CAS Login...")
      }
    }
  }
</script>

<style>
.accent-border {
  border: 1px solid #083c7c !important;
}
</style>
