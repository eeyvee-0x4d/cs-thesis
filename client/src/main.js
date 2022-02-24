import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './index.css'

// fontawesome
// import { library } from '@fortawesome/fontawesome-svg-core';
// import { faAngleRight } from '@fortawesome/free-solid-svg-icons';
// import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

// library.add(faAngleRight);

createApp(App)
	.use(router)
	.mount('#app');
