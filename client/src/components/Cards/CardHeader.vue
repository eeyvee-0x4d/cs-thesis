<template>
	<div class="relative flex flex-col border divide-y divide-solid">
		<div class="p-4 text-base text-left font-bold">
			<h1>Data Overview</h1>
		</div>
		<div v-if="isFetchingData" class="w-full m-auto p-4 text-center font-bold text-base">
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