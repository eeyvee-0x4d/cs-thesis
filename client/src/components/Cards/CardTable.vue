<template>
	<div class="relative w-full p-4">
		<div class="rounded-t mb-0 bg-transparent">
			<div class="flex flex-wrap items-center">
				<div class="relative pb-4 w-full max-w-full flex-grow flex-1">
					<h2 class=" text-base font-bold">
						{{ title }}
					</h2>
				</div>
			</div>
		</div>
		<div class="max-h-96 overflow-auto">
			<table class="w-full table-auto text-left break-text text-sm text-center">
				<!-- start table header -->
				<thead>
					<tr>
						<th>ID</th>
						<th>Date</th>
						<th>Tweet</th>
						<th>Sentiment</th>
					</tr>				
				</thead>
				<!-- end table header -->
				<!-- start table body -->
				<tbody class="">
					<tr v-for="item, index in data">
						<td>{{ index }}</td>
						<td>{{ item['Created-At'] }}</td>
						<td>{{ item['Text'] }}</td>
						<td>{{ (item['Sentiment'] === 1) ? "Positive" : "Negative" }}</td>
					</tr>
				</tbody>
				<!-- end table body -->
				<!-- start table footer -->
				<tfoot>
					
				</tfoot>
				<!-- end table footer -->
			</table>
		</div>
		<div class="py-2 flex justify-end">
			<button class="inline-block px-6 pt-2.5 pb-2 bg-blue-600 text-white font-medium text-xs leading-normal uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out flex align-center" @click="loadMore($event)">
				Load more
			</button>
		</div>
	</div>
</template>

<script>
	import { defineComponent, ref } from "vue";

	import axios from 'axios';

	export default defineComponent({
		name: 'CardTable',
		components: {
		},
		props: {
			title: { type: String, dafault: "Title"}
		},
		methods: {
			async fetchData() {
				let response = await axios.get(import.meta.env.VITE_DJANGO_BASE_URL + '/all_data/', {
					params: {
						page_number: this.page_number++,
						page_size: this.page_size
					}
				})

				if (response.statusText !== "OK") {
						throw new Error(`HTTP error! status: ${response.status}`)
					};

				return await response;
			},
			loadMore() {
				this.fetchData()
				.then((response) => {
					// this.data = Object.assign(this.data, JSON.parse(response.data))
					this.data = {
						...this.data,
						...JSON.parse(response.data)
					}
					console.log(this.data)
				})
				.catch()
			}
		},
		data() {
			return {
				data: {},
				page_number: 1,
				page_size: 20
			}
		},
		beforeMount() {
			this.fetchData()
				.then((response) => {
					this.data = (JSON.parse(response.data))
					// console.log(this.data)
				})
				.catch()
		},
		mounted() {
			// this.fetchData()
			// 	.then((response) => {
			// 		// console.log(response)
			// 	})
			// 	.catch()
		}
	});
	
</script>

<style>
	th {
		border:  1px solid #ddd;
		padding: .5rem;
	}

	td {
		border:  1px solid #ddd;
		padding: 0.5rem;
	}
</style>