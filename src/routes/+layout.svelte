<script lang="ts">
	// This is where the site sets its global CSS, and any elements that appear on all pages
	import '../app.css';
        import { base } from '$app/paths';
	interface Props {
		children?: import('svelte').Snippet;
	}

	let { children }: Props = $props();
	// If you want a custom font from fontsource, import it here, eg
	// import '@fontsource/my-custom-font/400.css';  // use My Custom Font at weight 400
</script>

<svelte:head>
	<base href="{base}" />
</svelte:head>

{@render children?.()}
