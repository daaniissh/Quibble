<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	import { defineCustomElements } from '@coreproject-moe/icons/loader';
	import Header from '$lib/components/header.svelte';
	import Sidebar from '$lib/components/sidebar.svelte';
	import Modals from '$lib/components/modals/index.svelte';

	let { children } = $props();

	onMount(() => {
		defineCustomElements();
	});
</script>

<Modals />
<main class="flex h-dvh w-dvw flex-col font-sans">
	<Header />
	<section class="mt-[3.75rem] flex">
		<div class="w-72">
			<Sidebar />
		</div>
		{@render children()}
	</section>
</main>
