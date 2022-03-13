<template>
	<nav  class="flex py-3 px-5 text-gray-700 bg-gray-50 rounded-lg border border-gray-200" aria-label="Breadcrumb">
		<ol class="inline-flex items-center space-x-1">
			<li class="inline-flex items-center" aria-current="page">
				<a class="text-gray-700 hover:text-gray-900 inline-flex items-center text-sm font-medium" href="/">
					Data Upload
				</a>
			</li>
			<div>
				<svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd"></path></svg>
			</div>
			<li class="inline-flex items-center">
				<div>
					<a class="text-gray-700 hover:text-gray-900 inline-flex items-center ml-1 text-sm font-medium" href="/Visualization">
						Visualization
					</a>
				</div>
			</li>
		</ol>
	</nav>
</template>

<script>
	import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'Breadcrumbs'
	});
</script>