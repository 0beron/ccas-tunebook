import type { LoadEvent } from '@sveltejs/kit';
import type { MungedFolder } from './folder.json/+server.js';

export const prerender = true;

// This is where the site gets the data for your tunes and sets
export function load({ fetch }: LoadEvent): Promise<{ folder: MungedFolder }> {
       const basePath = '/ccas-tunebook';
       return fetch(`${basePath}/folder.json`)
		.then((res) => res.json())
		.then((folder) => ({
			folder
		}));
}
