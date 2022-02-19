<template>
	<div class="container mb-4 border-b border-gray-200">
		<ul class="flex flex-wrap -mb-px">
			<li class="mr-2">
				<button class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-300" @click="currentTab(1)">
					Tab 1
				</button>
			</li>
			<li class="mr-2">
				<button class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-300" @click="currentTab(2)">
					Tab 2
				</button>
			</li>
			<li class="mr-2">
				<button class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-300" @click="currentTab(3)">
					Tab 3
				</button>
			</li>
			<li>
				<button class="inline-block py-4 px-4 text-sm font-medium text-center text-gray-500 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800 dark:hover:text-gray-300" @click="currentTab(4)">
					Tab 4
				</button>
			</li>
		</ul>
		<div class="p-3 mt-6 bg-white border">
			<div v-if="tab === 1">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolores ab ad fugiat laboriosam delectus eos ex quod vel temporibus nobis rerum necessitatibus, eligendi, provident unde a voluptas voluptatum. Magni, ex?</div>
			<div v-if="tab === 2">Lorem, ipsum dolor sit amet.</div>
			<div v-if="tab === 3">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Maxime quam, voluptatem sit, suscipit expedita iste aliquam. Praesentium maiores esse sit, voluptas ducimus inventore, qui eius harum quas non tenetur voluptate, magni quisquam nam doloribus ratione. Culpa inventore cumque eaque a in sequi eum minus aliquid voluptatem recusandae itaque praesentium, maiores distinctio laudantium? Aspernatur, dolore rem earum dolores, neque ullam atque numquam natus nulla distinctio explicabo, aliquam consequatur vitae repellat.</div>
			<div v-if="tab === 4">Lorem ipsum, dolor sit amet, consectetur adipisicing elit. Maxime, voluptate!</div>
		</div>
	</div>
</template>

<script>
	import { ref } from 'vue';

	export default {
		setup() {
			const tab = ref(1);
			const currentTab = (tabNumber) => (tab.value = tabNumber);

			return { tab, currentTab }
		}
	};
</script>