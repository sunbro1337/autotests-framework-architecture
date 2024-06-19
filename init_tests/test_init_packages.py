print("\nTest init of /packages")

print("\ncore")
import framework.core
framework.core.main.main()

print("\ntests_components")
import framework.tests_components
framework.tests_components.main.main()

print("\nrunner components")
import framework.runner_components
framework.runner_components.main.main()

print("\nmeta")
import framework.meta
framework.meta.main.main()
