<template>
	<nav class="flex justify-around items-center bg-white shadow-md" id="navbar">
		<div>
			<h1 class="text-3xl font-bold">{{ brand_name }}</h1>
		</div>
	</nav>
	
</template>

<script setup>
import {ref} from 'vue'

defineProps({
	brand_name: String
}) 
	
</script>

<style>
#navbar {
	min-height: 8vh;
}	
</style>