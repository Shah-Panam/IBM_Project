<?php
// Check if a file was uploaded
if (isset($_FILES['file'])) {
	$file = $_FILES['file'];

	// Check the file type
	if ($file['type'] == 'image/jpeg' || $file['type'] == 'image/png') {
		// Upload and compare image
		$target_dir = "uploads/";
		$target_file = $target_dir . basename($file['name']);
		move_uploaded_file($file['tmp_name'], $target_file);
		$command = "python compare_images.py " . $target_file;

		// Start the Python script in a separate process
		$descriptorspec = array(
			0 => array("pipe", "r"),  // stdin
			1 => array("pipe", "w"),  // stdout
			2 => array("pipe", "w"),  // stderr
		);
		$process = proc_open($command, $descriptorspec, $pipes);

		// Read the output of the Python script in real-time and output it to the web page
		while (!feof($pipes[1])) {
			$output = fgets($pipes[1]);
			echo "<pre>" . $output . "</pre>";
			ob_flush();
			flush();
		}

		// Close the process and pipes
		fclose($pipes[0]);
		fclose($pipes[1]);
		fclose($pipes[2]);
		proc_close($process);

	} elseif ($file['type'] == 'video/mp4') {
		// Upload and compare video
		$target_dir = "uploads/";
		$target_file = $target_dir . basename($file['name']);
		move_uploaded_file($file['tmp_name'], $target_file);
		$command = "python compare_videos.py " . $target_file;

		// Start the Python script in a separate process
		$descriptorspec = array(
			0 => array("pipe", "r"),  // stdin
			1 => array("pipe", "w"),  // stdout
			2 => array("pipe", "w"),  // stderr
		);
		$process = proc_open($command, $descriptorspec, $pipes);

		// Read the output of the Python script in real-time and output it to the web page
		while (!feof($pipes[1])) {
			$output = fgets($pipes[1]);
			echo "<pre>" . $output . "</pre>";
			ob_flush();
			flush();
		}

		// Close the process and pipes
		fclose($pipes[0]);
		fclose($pipes[1]);
		fclose($pipes[2]);
		proc_close($process);

	} else {
		echo "Invalid file type. Please upload an image or a video.";
	}
}
?>
