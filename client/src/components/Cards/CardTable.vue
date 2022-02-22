<template>
	<div class="relative w-full p-4">
		<div class="rounded-t mb-0 bg-transparent">
			<div class="flex flex-wrap items-center">
				<div class="relative w-full max-w-full flex-grow flex-1">
					<h2 class=" text-base font-bold">
						Chart Title
					</h2>
				</div>
			</div>
		</div>
		<table class="w-full table-auto text-left">
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
			<tbody>
				<tr v-for="item, index in data">
					<td>{{ index+1 }}</td>
					<td>{{ item.date }}</td>
					<td>{{ item.tweet }}</td>
					<td>{{ item.class }}</td>
				</tr>
			</tbody>
			<!-- end table body -->
			<!-- start table footer -->
			<tfoot>
				
			</tfoot>
			<!-- end table footer -->
		</table>
	</div>
</template>

<script>
	import { defineComponent, ref } from "vue";

	export default defineComponent({
		name: 'CardTable',
		components: {
		},
		data() {
			const data = [
				{
					"date": "01-01-2000",
					"tweet": "Hello World",
					"class": "Positive"
				},
				{
					"date": "01-01-2000",
					"tweet": "Hello World",
					"class": "Positive"
				}
			];

			return { data }
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