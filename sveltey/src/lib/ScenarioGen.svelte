<script>
    import { onMount } from 'svelte';

    export let sessionId;

    let GenScenario = "Loading scenario...";
    let error = null;

    async function fetchScenario() {
        try {
            const response = await fetch('https://zz1l696m-8000.uks1.devtunnels.ms/gen_scenario');
            if (!response.ok) {
                throw new Error('Failed to fetch scenario');
            }
            const data = await response.json();
            GenScenario = data.scenario;
            sessionId.set(data.session_id);
        } catch (err) {
            console.error('Error fetching scenario:', err);
            GenScenario = "Error loading scenario. Please refresh the page.";
            error = err.message;
        }
    }

    onMount(() => {
        fetchScenario();
    });
</script>

<div>
    <p class="Scenario"> 
        {#if error}
            {error}
        {:else}
            {GenScenario} <br><br>What will you do?
        {/if}
    </p>
</div>