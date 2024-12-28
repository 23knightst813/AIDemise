<script>
    import { onMount } from 'svelte';

    let GenScenario = "Loading scenario...";

    async function fetchScenario() {
        const response = await fetch('http://localhost:8000/gen_scenario');
        const data = await response.json();
        GenScenario = data.scenario;
    }

    onMount(() => {
        fetchScenario();
    });
</script>

<div>
    <p class="Scenario"> {GenScenario} <br><br>What will you do?</p>
</div>

<style>
    .Scenario {
        font-family: "bad script";
        font-size: large;
    }
</style>