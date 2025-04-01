<script lang="ts">
	import { FilterableSetsGrid, GlobalTranspositionButtons } from '@flyingcatband/tunebook';
	import { base } from '$app/paths';
	const baseWithTrailingSlash = base.endsWith('/') ? base : `${base}/`;
	let { data } = $props();
</script>

<svelte:head>
	<title>CCASTunebook</title>
</svelte:head>

<h1>Cambridge Ceilidh Allstars Tunebook</h1>
<GlobalTranspositionButtons showClefSwitcher />
<FilterableSetsGrid folder={data.folder} tuneFont="My Custom Font" basePath="{baseWithTrailingSlash}" />
