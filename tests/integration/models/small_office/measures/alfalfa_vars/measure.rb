# insert your copyright here

# see the URL below for information on how to write OpenStudio measures
# http://nrel.github.io/OpenStudio-user-documentation/reference/measure_writing_guide/

# start the measure
class AlfalfaVariables < OpenStudio::Measure::ModelMeasure
  # human readable name
  def name
    return 'AlfalfaVariables'
  end

  # human readable description
  def description
    return 'Add custom variables for Alfalfa'
  end

  # human readable description of modeling approach
  def modeler_description
    return 'Add EMS global variables required by Alfalfa'
  end

  # define the arguments that the user will input
  def arguments(model)
    args = OpenStudio::Measure::OSArgumentVector.new
    return args
  end

  # define what happens when the measure is run
  def run(model, runner, user_arguments)
    super(model, runner, user_arguments)

    # Alfalfa inputs
    # These can be set through the Alfalfa API, they will be available as OutputVariables
    # in the simulation. Use them as you will
    # Also see comments on the create_input method
    test_point_1 = OpenStudio::Model::EnergyManagementSystemGlobalVariable.new(model, 'Test_Point_1')
    runner.alfalfa.exposeFromObject(test_point_1, "Test_Point_1")
    return true
  end
end

# register the measure to be used by the application
AlfalfaVariables.new.registerWithApplication
