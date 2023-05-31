import { createRouter, createWebHistory } from 'vue-router'
import DefaultView from '@/layouts/default/Default.vue'
import Home from '@/views/Home.vue'
import Profile from '@/views/Profile.vue'
import NotFound from '@/views/NotFound.vue'


const routes = [
  {
    path: '/',
    component: DefaultView,
    children: [
      {
        path: '',
        name: 'Home',
        component: Home,
      },
      {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component:  NotFound,
      },
    ],
  },
  {
    component: Profile,
    path: '/user/urls',
    name: 'Urls',
    meta: {
      title: 'Profile'
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
