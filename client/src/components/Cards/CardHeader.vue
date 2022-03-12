<template>
	<div class="relative flex flex-col border divide-y divide-solid">
		<div class="p-4 text-base text-left font-bold">
			<h1>Data Overview</h1>
		</div>
		<div v-if="isFetchingData" class="w-full m-auto p-4 text-center font-bold text-base">
			<svg role="status" class="inline mr-2 w-6 h-6 text-gray-200 animate-spin fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
			    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
			    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
			</svg>
			<span>
				Loading data...
			</span>
		</div>
		<div v-else class="grid grid-cols-4 p-4 place-content-evenly divide-x">
			<div>
				<CardStats ref="cardStat1"/>
			</div>
			<div>
				<CardStats ref="cardStat2"/>
			</div>
			<div>
				<CardStats ref="cardStat3"/>
			</div>
			<div>
				<CardStats ref="cardStat4"/>
			</div>
		</div>
	</div>
</template>

<script>
	import CardStats from './CardStats.vue'
	import CardBarChart from './CardBarChart.vue'

	import { ref } from 'vue';

	import axios from 'axios';

	export default {
		name: 'CardHeader',
		components: {
			CardStats
		},
		methods: {
			test() {
				console.log('Hello')
			},
			async fetchData() {
				this.isFetchingData = true

				let response = await axios.get(import.meta.env.VITE_DJANGO_BASE_URL + '/data_overview/');

				if (response.statusText !== "OK") {
					throw new Error(`HTTP error! status: ${response.status}`)
				};

				this.isFetchingData = false

				return await response;
			},
			abbrNum(number, decPlaces) {
			    // 2 decimal places => 100, 3 => 1000, etc
			    decPlaces = Math.pow(10,decPlaces);

			    // Enumerate number abbreviations
			    var abbrev = [ "k", "m", "b", "t" ];

			    // Go through the array backwards, so we do the largest first
			    for (var i=abbrev.length-1; i>=0; i--) {

			        // Convert array index to "1000", "1000000", etc
			        var size = Math.pow(10,(i+1)*3);

			        // If the number is bigger or equal do the abbreviation
			        if(size <= number) {
			             // Here, we multiply by decPlaces, round, and then divide by decPlaces.
			             // This gives us nice rounding to a particular decimal place.
			             number = Math.round(number*decPlaces/size)/decPlaces;

			             // Add the letter for the abbreviation
			             number += abbrev[i];

			             // We are done... stop
			             break;
			        }
			    }

			    return number;
			},
		},
		data() {
			let isFetchingData = false

			return {
				isFetchingData
			}
		},
		mounted() {
			this.fetchData()
				.then(response => {
					console.log(response)

					this.$refs.cardStat1.kpiHeader = 'Pfizer'
					this.$refs.cardStat1.kpiBigNumber = (response.data.pfizer === null) ? 'n.d' : this.abbrNum(response.data.pfizer, 1)
					this.$refs.cardStat1.kpiSubHeader = (response.data.pfizer === null) ? '' : 'Tweets'

					this.$refs.cardStat2.kpiHeader = 'Sinovac'
					this.$refs.cardStat2.kpiBigNumber = (response.data.sinovac === null) ? 'n.d' : this.abbrNum(response.data.sinovac, 1)
					this.$refs.cardStat2.kpiSubHeader = (response.data.sinovac === null) ? '' : 'Tweets'

					this.$refs.cardStat3.kpiHeader = 'AstraZeneca'
					this.$refs.cardStat3.kpiBigNumber = (response.data.astrazeneca === null) ? 'n.d' : this.abbrNum(response.data.astrazeneca, 1)
					this.$refs.cardStat3.kpiSubHeader = (response.data.astrazeneca === null) ? '' : 'Tweets'

					this.$refs.cardStat4.kpiHeader = 'Moderna'
					this.$refs.cardStat4.kpiBigNumber = (response.data.moderna === null) ? 'n.d' : this.abbrNum(response.data.moderna, 1)
					this.$refs.cardStat4.kpiSubHeader = (response.data.moderna === null) ? '' : 'Tweets'


				})
				.catch()
		}
	}
</script>