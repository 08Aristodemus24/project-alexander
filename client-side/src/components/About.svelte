<script>
    import { onMount } from "svelte";

    let is_mounted = false;
    onMount(async () => {
        is_mounted = true
    });

</script>
<section id="about-section">
    <div class="about-content">
        <div class="about-header-container">
            <h1>About me</h1>
            <p>
                I am a currently a student specializing<br>
                in machine learning engineering and an<br>
                aspiring computational immunologist
            </p>
            <p>
                Albeit I'm still in this continuous<br>
                journey of learning here's some<br>
                technologies I picked up
            </p>
        </div>
        <div class="anims-container">
            <!-- render only video if component has mounted to prevent freezing -->

            {#if is_mounted === true}
                <video autoplay muted loop>
                    <source src="https://github.com/08Aristodemus24/project-alexander/raw/master/client-side/src/assets/mediafiles/Skillsfinal.mp4" type="video/mp4">
                </video>
            {/if}
        </div>
    </div>
</section>